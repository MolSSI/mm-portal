---
title: "Data parsing & validation"
draft: true
hideLastModified: true
showInMenu: false
summaryImage: "images/icon.png"
developer: Samuel Ellis, Andrew Abi-Mansour
summary: "Parsing and validating schemas with pydantic"
---

# Prerequisites

This tutorial explains how pydantic is used in MMIC to parse and validate schemas. This tutorial assumes you're familiar with the python programming language
and the basics of MM components. If not, you should 1st go over the "getting started" [tutorial](/tutorials/getting_started).

# Introduction 

<p id="data_valid">Python does not inherently enforce typing of functions or variables at
runtime. Instead, python allows for type hints to be specified in order to
inform users and other developers what is expected by a function and what
is provided.</p>

[Pydantic](https://pydantic-docs.helpmanual.io/) is a python package
designed to expand on the concept of typing in python. It is used to
enforce type hints in python, allowing objects to be validated during
runtime. 

For primitive types, that is `str`, `int`, `float`, and `bool` , this
simply takes the form of an annotation.


{{< code language="python" line-numbers="false">}}
def name_typing(name: str) -> str:
    return name
{{< /code >}}

The variable `name` is annotated with a `:` followed by the type, in this
case, we expect a name to be a `str`. The function's return type is also
hinted at. After the parameters, but before the `:` we use an `->` to
denote there is a type hint, followed by the type. In this case we are
using a string as well.


Here we test the function with a couple of variables.

{{< code language="python" line-numbers="false">}}
name_str = 'John'
name_num = 5
print(name_typing(name_str))
print(name_typing(name_num))
{{< /code >}}

We get the following output:

{{< code language="python" line-numbers="false">}}
John
5
{{< /code >}}

Python does not enforce the type, so the function will return the variable
and print both out correctly. If we want to have more complex types, such
as `List`, `Dict`, `Union`, or `Optional` types, we need to utilize
python's `typing` library.

{{< code language="python" line-numbers="false">}}
from typing import List, Dict, Union, Optional
{{< /code >}}

We can then utilize them in type hints.

{{< code language="python" line-numbers="false">}}
registrant_names: List[str]
birthday: Optional[str]
{{< /code >}}


# Pydantic BaseModel

TODO: Cover Base Pydantic model, and why it is used.

Each component in MMIC has two schema, an Input Schema and an Output Schema.
Depending on the component the two schemas may be the same or different. To
define a schema we utilize a pydantic [model](https://pydantic-docs.helpmanual.io/usage/models) to create a set of variables
with specific types to ensure that a component can run for a given input
as long as it conforms to the Input Schema.

The model used by pydantic is the `BaseModel`. We can import this from
pydantic and then inherit it when we create a schema.

{{< code language="python" line-numbers="false">}}
from pydantic import BaseModel
class Schema(BaseModel):
{{< /code >}}

The benefits of inhertiting the BaseModel is the validation that comes
with it. When an instance of a class model is created from a schema, the
values assigned to each variable in this object are validated against their assigned
type.


{{< code language="python" line-numbers="false">}}
class SchemaExample(BaseModel):
    var1: int
    var2: str
    var3: Optional[float]
{{< /code >}}


To provide further information about each variable, we can utilize the
Field method from pydantic.

{{< code language="python" line-numbers="false">}}
class SchemaExample(BaseModel):
    var1: int = Field(..., description="This is the first variable for the example schema.")
    var2: str = Field(..., description="This is the second variable for the example schema.")
    var3: Optional[float]
{{< /code >}}

The first argument in the `Field` method is a positional argument for the
default value of the variable. Entering `...` for the default value will
let pydantic know the variable has no default value. There are a number of
keyword arguments for the `Field` method that can be found in the
[Pydantic](https://pydantic-docs.helpmanual.io/) documentation, but we
will mention `description` as a useful one to include, as it allows for
more detailed documentation for each variable.


For a more concrete example, we can look at the `DockInput` schema for molecular docking.

{{< code language="python" line-numbers="false">}}
from mmelemental.models.base import SimBase
from mmelemental.models.molecule import Molecule
from typing import List, Optional, Tuple, Union
from pydantic import Field

class DockInput(SimBase):
    ligand: Molecule = Field(
        ..., 
        description="Molecule model for a candidate ligand (e.g. drug)."
    )
    receptor: Molecule = Field(
        ..., 
        description="Molecule model for a receptor (e.g. protein)."
    )
    searchSpace: Optional[List[Tuple[float, float, float, float, float, float]]] = Field(
        None,
        description="A 3D box defined by (xmin, xmax, ymin, ymax, zmin, zmax).
        The search space effectively restricts where the movable atoms should lie."
    )
{{< /code >}}

The first thing to notice is that we did not inherit from Pydantic's
`BaseModel` class. MMIC utilize an extension of the `BaseModel`, and the
`DockInput` inherits a further extension, the `SimBase`, which is a
basic simulation schema. Since our inheritance tree includes the
`BaseModel` we will enforce typing on the variables within the schema.
Similar to normal inheritance, we inherit all of the typed variables from
our parent class.

Therefore, the `DockInput` contains all the typed variables from the
`SimBase` schema, and adds three new variables, `ligand` which is of type
`Molecule`, `receptor` which is also of type `Molecule` and `searchSpace`
which is an optional `Tuple` of `floats` that defines a 3D box to search
within.

# Schema Validation

TODo: Cover basic validation being performed on all the variables in the schema.

TODO: Cover how to add custom validators to a variable in a schema.


Pydantic performs validation on all the variables in a schema. By default,
this means if you specify a type for a variable and pass it a value of a
different type, it will provide you an error message with useful
information. Note that we use typed schema variables as keyword arguments,
not positional arguments.


{{< tabsCode
    file1="/content/tutorials/data_validation/code/run.md" title1="run" language1="python" icon1="python"
    file2="/content/tutorials/data_validation/code/output.md" title2="output" language2="shell" icon2="shell"
>}}

We can see that it reported a single validation error. Pydantic will try
and perturb primitive types if they have a simple conversion. In this
case, since var2 is a string type, and an integer, `5` can easily be
converted losslessly by python, it will assume `5` was meant to be passed
as a string. However, since the first variable is looking for an `int` and
it was passed a string, it rovides information on the variable that had an
error, and what the expected type was.

As schema become more complicated, simple assignment validation may no
longer be sufficient. In addition, you may wish to assign additional
conditions to the values of variables outside of simply their type.
Pydantic supports custom validators to cover these cases.

To write a custom validator, you must import a few additional things from
pydantic.

{{< code language="python" line-numbers="false">}}
from pydantic import validator, ValidationError
{{< /code >}}

This will import the decorator `@validator` which is used to specify a
method is used for validation, and `ValidationError` can be used to check
if an error was thrown during validation.

{{< code language="python" line-numbers="false">}}
from pydantic import BaseModel, validator, ValidationError

class SchemaExample(BaseModel):
    var1: int = Field(..., description="This is the first variable for the example schema.")
    var2: str = Field(..., description="This is the second variable for the example schema.")
    var3: Optional[float]
    
    @validator('var2')
    def var2_alphanumeric(cls, v):
        assert v.isalnum(), 'var2 must be alphanumeric'
        return v
{{< /code >}}

We have added a custom validator to ensure that `var2` is only made of
alphanumeric characters. We use the decorator `@validator('var2')` to
specify that the following function should be used to perform validation
on the variable `var2`. We pass the `cls` since this method is used on the
`SchemaExample` class and not on an instanced object and by pydantic
convention use `v` for the value that is being assigned to the variable.

Here we can test the validator to ensure it is working.

{{< code language="python" line-numbers="false">}}
example = SchemaExample(var1=5, var2='hellos12345_@#$')

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pydantic/main.py", line 362, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for
SchemaExample

var2
  var2 must be alphanumeric (type=assertion_error)
{{< /code >}}

A more thorough description of validators and how to write custom ones can
be found within the [pydantic
documentation](https://pydantic-docs.helpmanual.io/usage/validators/).

# ProtoModel

For the MMIC poject, we utilize an extension of the pydantic BaseModel.
This was originally developed for the QCArchive project and can be found
within the
[QCElemental](https://github.com/MolSSI/QCElemental/blob/master/qcelemental/models/basemodels.py)
package.

Any schema based on this `ProtoModel` gains a few additional features.

It covers a few ways to parse in a model. First a model object can be
parsed in from a raw string or bytes using the `parse_raw()` method. This
is useful if the values for a model are contained in a serialized form,
such as `json` or `msgpack-ext`. A model can also be parsed from a file
using the `parse_file()` method. Current supported encodings are `json`,
`msgpack-ext`,  and `pickle` files.

Similarly, a model can be serialized into `json`, `json-ext`, or
`msgpack-ext`. This allows the model to be shipped around as a set of
bytes or as a string.

Finally, `ProtoModel` allows for the comparison of instanced objects. The
`self.compare()` method can be used to compare the current object to a given
object recursively.
