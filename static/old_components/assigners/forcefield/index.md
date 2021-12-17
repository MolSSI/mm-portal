---
title: "mmic_ffpa"
draft: true
hideLastModified: false
developer: Andrew Abi-Mansour
showInMenu: false
summary: "Assigns force field parameters to molecules based on existing force fields"
tags: ["Assigners", "ForceFields"]
---

{{< siteBlue "Unreleased" "https://github.com/MolSSI/mmic_ffpa" >}}
This component is *usable* with relatively *stable* **schemas**. However, it is *buggy*.

[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic_ffpa/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic_ffpa/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic_ffpa/branch/master/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic_ffpa/branch/master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MolSSI/mmic_ffpa.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/mmic_ffpa/context:python)
{{< /siteBlue >}}

# Design

#### Models
This package provides 4 models derived from MMSchema. The input models are:
- [ParamInput](https://github.com/MolSSI/mmic_ffpa/blob/master/mmic_ffpa/models/input.py): external input that defines the input molecule and which force field to use
- [ComputeInput](https://github.com/MolSSI/mmic_ffpa/blob/master/mmic_ffpa/models/input.py): internal input used for running compute

The output models are:
- [ParamOutput](https://github.com/MolSSI/mmic_ffpa/blob/master/mmic_ffpa/models/output.py): external output that stores the molecule and force field objects
- [ComputeOutput](https://github.com/MolSSI/mmic_ffpa/blob/master/mmic_ffpa/models/output.py): internal output used for storing compute output

{{< figure src="images/component.png" width="1120" caption="Schematic diagram of the component and its data (schemas) flow.">}}

#### Components
There are 3 components used for assigning the force field parameters to a given MMSchema molecule: 
- [PrepComponent](https://github.com/MolSSI/mmic_ffpa/blob/master/mmic_ffpa/components/prep_component.py#L7): pre-processes and validates input needed for compute
- [ComputeComponent](https://github.com/MolSSI/mmic_ffpa/blob/master/mmic_ffpa/components/post_component.py#L5): assigns the force field parameters by calling a specific engine e.g. gmx
- [PostComponent](https://github.com/MolSSI/mmic_ffpa/blob/master/mmic_ffpa/components/post_component.py#L5): post-processes the output

# Snippet
{{< tabsCode
    file1="/content/components/assigners/forcefield/models.md" title1="Models" language1="python" icon1="python"
    file2="/content/components/assigners/forcefield/components.md" title2="Components" language2="python" icon2="python"
>}}

# Requirements
- [MMElemental](https://github.com/MolSSI/MMElemental)
- [MMIC](https://github.com/MolSSI/mmic)
- [FF translator](/tags/translators)
- [Mol translator](/tags/translators)
