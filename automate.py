from enum import Enum
import sys
import re
from datetime import date, datetime
import json
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Set
from pathlib import Path
import shutil
import uuid
import requests


timeformat = "%Y-%m-%d"

assert (
    sys.version_info.major == 3 and sys.version_info.minor >= 8
), "python>=3.8 required"


class TagEnum(Enum):
    ForceFields = "forcefields"
    Assigners = "assigners"
    Gromacs = "gromacs"
    Strategy = "strategy"
    Tactic = "tactic"
    Util = "util"
    Simulators = "simulators"
    MMSchema = "mmschema"
    Translators = "translators"

def random_file(suffix="", *, path=".", unique=True):
    """Returns a random file name generated from a universally
    unique identifier (UUID).

    Parameters
    ----------
    suffix: str
        Filename suffix
    path: str
        Path to filename
    unique: bool
        Ensures filename does not exist on disk
    Return
    ------
    filename: str
        Absolute filename path
    """
    fname = str(uuid.uuid4()) + suffix
    fpath = Path(fname)

    if path:
        fpath = Path(path) / fpath

    if unique:
        if fpath.is_file():
            return random_file(suffix, path=path, unique=unique)

    return fpath


class CompModel(BaseModel):
    title: str = Field(...)
    link: str = Field(...)
    tags: List[TagEnum] = Field(...)
    summary: str = Field(...)
    developer: str = Field(...)
    date: Optional[str] = Field(date.today().strftime(timeformat))
    image: Optional[str] = Field(None)

    class Config:
        allow_mutation: bool = False
        extra: str = "forbid"
        serialize_default_excludes: Set = set()
        serialize_skip_defaults: bool = False
        force_skip_defaults: bool = False

    def dict(self, **kwargs):
        kwargs["exclude"] = (
            kwargs.get("exclude", None) or set()
        ) | self.__config__.serialize_default_excludes
        kwargs.setdefault("exclude_unset", self.__config__.serialize_skip_defaults)
        if self.__config__.force_skip_defaults:
            kwargs["exclude_unset"] = True

        data = super().dict(**kwargs)
        if data["image"]:
            data["image"] = Path(data["image"]).name

        return data

    @validator("link")
    def _valid_link(cls, v):
        res = requests.get(v)
        assert res.status_code == 200, "URL {link} is invalid!"
        return v

    @validator("image")
    def _valid_image(cls, v):
        if v.startswith("http"):
            ext = v.split(".")[-1]
            res = requests.get(v, stream=True)
            assert res.status_code == 200, f"Could not download file {v}."
            res.raw.decode_content = True
            tmpdir = Path("static/components/tmp")
            if not tmpdir.is_dir():
                tmpdir.mkdir()
            pfile = random_file(suffix="." + ext, path=tmpdir)
            v = str(pfile.absolute())

            with open(v, "wb") as fileobj:
                shutil.copyfileobj(res.raw, fileobj)
        else:
            pfile = Path(v)

        assert pfile.is_file(), f"Image file {str(p)} does not exist!"

        return v

    @validator("date")
    def _valid_time(cls, v):
        try:
            validtime = datetime.strptime(v, timeformat)
        except ValueError:
            raise ValueError
        return v


with open("static/components/data.json", "r") as fileobj:
    data = json.load(fileobj)

path = Path("content/components")
assert path.is_dir(), "Dir content/components does not exist!"

for comp_name, comp in data.items():

    comp_model = CompModel(title=comp_name, **comp)
    comp = comp_model.dict()

    data = {}

    for key, val in comp.items():
        if isinstance(val, Enum):
            data[key] = val.name
        elif isinstance(val, list):
            data[key] = "[" + ",".join([item.name for item in val]) + "]"
        else:
            data[key] = val

    cpath = path / comp_model.title
    if cpath.is_dir():
        shutil.rmtree(cpath)

    cpath.mkdir()

    if comp_model.image:
        text = "title: {title}\ndate: {date}\ndraft: true\nhideLastModified: true\nshowInMenu: false\nsummaryImage: {image}\nsummary: {summary}\nlink: {link}\ntags: {tags}\n".format(
            **data
        )
        shutil.copy(comp_model.image, cpath)
    else:
        text = "title: {title}\ndate: {date}\ndraft: true\nhideLastModified: true\nshowInMenu: false\nsummary: {summary}\nlink: {link}\ntags: {tags}\n".format(
            **data
        )

    fpath = cpath / "index.md"
    with open(fpath, "w") as fileobj:
        fileobj.write("---\n")
        fileobj.write(text)
        fileobj.write("---")

    tmpdir = Path("static/components/tmp")
    if tmpdir.is_dir():
        shutil.rmtree(tmpdir)
