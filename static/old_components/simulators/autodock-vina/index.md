---
title: "mmic_autodock_vina"
developer: Andrew Abi-Mansour
draft: true
hideLastModified: false
showInMenu: false
summaryImage: "images/icon.png" 
summary: "Performs molecular docking with AutoDock Vina"
tags: ["Simulators", "Tactic"]
---

{{< siteBlue "Unreleased" "https://github.com/MolSSI/mmic_autodock_vina" >}}
This component is *usable* with a *stable* **API** and **schemas**. However, it is *buggy*.

[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MolSSI/mmic_autodock_vina/workflows/CI/badge.svg)](https://github.com/MolSSI/mmic_autodock_vina/actions?query=workflow%3ACI)
[![codecov](https://codecov.io/gh/MolSSI/mmic_autodock_vina/branch/master/graph/badge.svg)](https://codecov.io/gh/MolSSI/mmic_autodock_vina/branch/master)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/MolSSI/mmic_autodock_vina.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/MolSSI/mmic_autodock_vina/context:python)

{{< /siteBlue >}}

# Design
The 2 main models used by this component are:
- [DockInput](https://github.com/MolSSI/mmic_docking/blob/master/mmic_docking/models/input.py#L8)
- [DockOutput](https://github.com/MolSSI/mmic_docking/blob/master/mmic_docking/models/input.py#L14)

Both models are provided by the [mmic_docking](/components/simulators/docking) component.

{{< figure src="images/component.png" width="1318" caption="Schematic diagram of the component and its data (schemas) flow.">}}

There are 3 components used in this package for associating the force field parameters to a given MMSchema molecule: 
- [AutoDockPrep](https://github.com/MolSSI/mmic_docking/blob/master/mmic_docking/components/prep_component.py#L7): pre-processes the input for compute
- [AutoDockCompute](https://github.com/MolSSI/mmic_docking/blob/master/mmic_docking/components/post_component.py#L5): run the compute
- [AutoDockPost](https://github.com/MolSSI/mmic_docking/blob/master/mmic_docking/components/post_component.py#L5): post-processes the output

# Snippet
{{< tabsCode
    file1="/content/components/simulators/autodock-vina/models.md" title1="Models" language1="python" icon1="python"
    file2="/content/components/simulators/autodock-vina/components.md" title2="Components" language2="python" icon2="python"
>}}

# Requirements
- [MMElemental](https://github.com/MolSSI/MMElemental)
- [MMIC](https://github.com/MolSSI/mmic)
- [Mol translator](http://localhost:1313/tags/translators)
- [Autodock Vina](https://anaconda.org/bioconda/autodock-vina)
