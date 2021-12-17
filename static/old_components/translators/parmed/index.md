---
title: "mmic_parmed"
date: 2021-02-12
draft: true
developer: Andrew Abi-Mansour
hideLastModified: false
showInMenu: false
summaryImage: "images/icon.png"
summary: "Provides translators between MMSchema and ParmEd"
tags: ["Translators", "MMSchema", "Tactic"]
---

{{< siteBlue "Unreleased" "https://github.com/MolSSI/mmic_parmed" >}}
This component is *usable* with a *stable* **API** and **schemas**.

[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic_parmed/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic_parmed/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic_parmed/branch/main/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic_parmed/branch/main)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MolSSI/mmic_parmed.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/mmic_parmed/context:python)

{{< /siteBlue >}}

# Design
This package provides translators between [MMSchema](/mmschema) and [ParmEd](https://github.com/ParmEd/ParmEd) for the following objects: molecule and forcefield. The model for
each object is, respectively: ParmedMol and ParmedFF. The `from_schema` and `to_schema` methods in each model use translation components to convert between MMSchema and ParmEd.

<img src="https://github.com/MolSSI/mmic_parmed/raw/main/mmic_parmed/data/imgs/component.png">

# Schemas

# Inheritance
This component is a subcomponent of [mmic_translator](https://github.com/MolSSI/mmic_translator).



### Copyright
Copyright (c) 2021, MolSSI
