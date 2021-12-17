---
title: "MMIC"
date: 2019-06-17T23:53:00+01:00
draft: true
hideLastModified: true
img_path: images/mmic.png
showInMenu: false
# no need for the "summary" parameter as it is not displayed in any previews
---

# What is this portal about?
...

# What is MMIC?
The Molecular Mechanics Interoperable Components (MMIC) project provides a standard for input and output of MM programs by defining the scientific and computational stages of classical MM pipelines, but leaving the implementation up to the developer/user. MMIC attempts to define the "what" of scientific stages without restricting the "how" i.e. MMIC defines only the input and output the implementation must conform to so that end-users can swap out different implementations with minimal effort in their existing pipelines, or workflow tools of their preference. The components themselves allow users to speed up most of their pipelines by integrating the expertise from component developers, letting them focus on the parts of their research they are experts in.

This allows reproducibility from statically defined and shareable components, experimentation to find a quality series of components for specific problems and systems, and a mechanism for quality methodological assessment without the need for deep scientific expertise.

The base class in MMIC is the abstract Base Component that is inherited by all MM Component blueprints. For each scientific problem, a blueprint is defined that specifies what the component seeks to achieve, along with the necessary inputs and outputs. This component is implemented to satisfy the scientific problem by any number of users/developers.
