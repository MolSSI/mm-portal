---
title: "Getting started"
draft: true
hideLastModified: true
showInMenu: false
summaryImage: "images/icon.png"
summary: "Creating your 1st component"
---

# Prerequisites

It is recommended that you familiarize yourself with the python programming language and best practices in software engineering before delving into this tutorial.
The MolSSI [education hub](http://education.molssi.org/resources.html) provides plenty of materials on software development that make this tutorial easier to follow
and understand.

# Package creation

There are infinite ways you could build your own components in MMIC. An easy and quick way to get started is by using
[cookiecutter](https://github.com/cookiecutter/cookiecutter), which you can install via pip and then interactively run to create a git repository:
{{< code language="bash" line-numbers="false">}}
pip install cookiecutter
cookiecutter gh:molssi/cookiecutter-mmic
{{< /code >}}

After you're done answering all the questions, you should end up with a git directory that has a tree structure similar to this:

{{< code language="bash" line-numbers="false">}}
.
├── mmic_pkg
│   ├── components
│   │   ├── component.py
│   │   └── __init__.py
│   ├── data
│   │   ├── look_and_say.dat
│   │   └── README.md
│   ├── __init__.py
│   ├── mmic_mmic_pkg.py
│   ├── models
│   │   ├── __init__.py
│   │   └── model.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_mmic_pkg.py
│   └── _version.py
├── setup.py
...
{{< /code >}}

The MMIC cookiecutter is based on the CMS cookiecutter, which provides a lot of useful tools for continuous integration and package management. Of notable importance to MMIC are the 
`pkg_name/models` dir which stores all the models, and the 'components' dir which stores all the components.

# Package customization
For the purpose of this tutorial, we're going to use the `mmic_pkg` template to create a component that computes the number of atoms from a given molecular formula. 
Let's begin by 1st defining the input and output models for this component.

## Models
In the 'pkg_name/models' dir, you'll find a **model.py** file which defines a `Model` shown in the **Model-template** tab.

{{< tabsCode
    file1="/content/tutorials/MMIC/getting_started/code/model-original.md" title1="Model-template" language1="python" icon1="python"
    file2="/content/tutorials/MMIC/getting_started/code/model.md" title2="Model" language2="python" icon2="python"
>}}

We're going to define 2 required fields: `mol_formula` of type `str` in `InputModel` and `natoms` of type `int` in `OutputModel` as shown in the **Model** tab.
 
## Components

Now that we've defined our models, we need to work on the component that uses the models. 
In the 'pkg_name/components' dir, you'll find a **component.py** that defines a `Component` class shown in the **Component-template** tab.

{{< tabsCode
    file1="/content/tutorials/MMIC/getting_started/code/component-original.md" title1="Component-template" language1="python" icon1="python"
    file2="/content/tutorials/MMIC/getting_started/code/component.md" title2="Component" language2="python" icon2="python"
>}}

Note the 3 required methods already defined in this component:
- input: classmethod that returns the input schema/model
- output: classmethod that returns the output schema/model
- execute: method that recevies an input modal, does the execution, and returns an output model 

Note also that `Component` is a subclass of `GenericComponent`, which under the hood uses the `cls.input` to validate the input data and `cls.output` to validate the
output data `self.execute` returns. This is achieved via the `GenericComponent.compute` method, which should not be overwritten. Otherwise, developers can attach any other 
method of their choice to `Component`. For more info on how components are designed, see the [MMIC](https://github.com/MolSSI/mmic) repository.

We're going to modify the `self.execute` method by counting the number of atoms in the supplied molecular formula, then return the output model. Note that the boolean variable `True` 
signifies successful execution. The code is shown in the **Component** tab.

## Putting it altogether

You can now use **setup.py** included with **mmic_pkg** to install the component. From the root directory run:

{{< code language="bash" line-numbers="false">}}
pip install .
{{< /code >}}

Using this component is straight forward as shown below.
{{< tabsCode
    file1="/content/tutorials/MMIC/getting_started/code/run-valid.md" title1="Valid" language1=python icon1="python"
    file2="/content/tutorials/MMIC/getting_started/code/run-invalid.md" title2="Invalid" language2=python icon2="python"
>}}

In the **Valid** tab, the `mol_formula` is of type `str`, which leads to successful execution:
{{< code language="bash" line-numbers="false">}}
  Number of atoms in CH4 is 5
{{< /code >}}

In the **Invalid** tab, the `mol_formula` is a `list`, which causes pydantic to raise a validation error.

{{< code language="bash" line-numbers="false">}}
  Traceback (most recent call last):
  File "run.py", line 5, in <module>
    input = mmic_pkg.models.InputModel(mol_formula=mfor)
  File "pydantic/main.py", line 400, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for InputModel
mol_formula
  str type expected (type=type_error.str)
{{< /code >}}

As you can see, components in the MMIC world use pydantic to parse and validate the input and output data they receive and produce. For more information on data validation, see the [tutorial](/tutorials/data_validation/) on data validation.

# Package deployment

You can package and deploy your component the same way you would with any other python package. See the official [python](http://packaging.python.org) resource for more info on packages and the 
Python Package Index (PyPi).
