---
title: "mmic_docking"
developer: Levi Naden, Sam Ellis, Andrew Abi-Mansour
draft: true
hideLastModified: false
showInMenu: false
summaryImage: "images/icon.png" 
summary: "Performs molecular docking with any of the supported docking components"
tags: ["Simulators", "Strategy"]
---

{{< siteBlue "Experimental" "https://github.com/MolSSI/mmic_docking" >}}
This component is *usable* with a *stable* **API** and **schemas**. However, it is *buggy*.
{{< /siteBlue >}}

# Design
The 2 main models used by this component are:
- [DockInput](https://github.com/MolSSI/mmic_docking/blob/master/mmic_docking/models/input.py#L8)
- [DockOutput](https://github.com/MolSSI/mmic_docking/blob/master/mmic_docking/models/input.py#L14)

Both models are provided by the [mmic_docking](/components/simulators/docking) component.

{{< figure src="images/component.png" width="1318" caption="Schematic diagram of the component and its data (schemas) flow.">}}

There are 3 components used in this package for associating the force field parameters to a given MMSchema molecule: 
- [PrepComponent](https://github.com/MolSSI/mmic_docking/blob/master/mmic_docking/components/prep_component.py#L7): pre-processes the input for compute
- [ComputeComponent](https://github.com/MolSSI/mmic_docking/blob/master/mmic_docking/components/post_component.py#L5): run the compute
- [PostComponent](https://github.com/MolSSI/mmic_docking/blob/master/mmic_docking/components/post_component.py#L5): post-processes the output

# Snippet
{{< tabsCode
    file1="/content/components/simulators/docking/input.md" title1="Input" language1="python" icon1="python"
    file2="/content/components/simulators/docking/api.md" title2="API" language2="python" icon2="python"
    file3="/content/components/simulators/docking/output.md" title3="Output" language3="python" icon3="python"
>}}

# Requirements
- [MMElemental](https://github.com/MolSSI/MMElemental)
- [MMIC](https://github.com/MolSSI/mmic)
- [Mol translator](http://localhost:1313/tags/translators)
- [Autodock Vina]
