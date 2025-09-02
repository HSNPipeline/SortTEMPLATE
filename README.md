# SortTEMPLATE

Template structure for spike sorting microwire data from human subjects.

[![Template](https://img.shields.io/badge/template-HSNPipeline/SortTEMPLATE-yellow.svg)](https://github.com/HSNPipeline/SortTEMPLATE)
[![Convert](https://img.shields.io/badge/data-ConvertTEMPLATE-lightgrey)](https://github.com/HSNPipeline/ConvertTEMPLATE)
[![Analysis](https://img.shields.io/badge/analysis-AnalyzeTEMPLATE-lightgrey)](https://github.com/HSNPipeline/AnalyzeTEMPLATE)

## TEMPLATE DESCRIPTION

This is a template repository for running spike sorting on a dataset, using the
[combinato](https://github.com/jniediek/combinato) spike sorter.

This template follows the general purpose
[ProjectTemplate](https://github.com/structuredscience/ProjectTemplate)
layout from
[StructuredScience](https://github.com/structuredscience/).

For information on how to use this template in a project, see the
[HSNPipeline Guide](https://github.com/HSNPipeline/Overview/blob/main/Guide.md).

Note: if copying this template for use, this section can be removed.

## Overview

**Provide an overview of the data here, for example:**

This repository manages spike sorting for the XX task / project.

## Requirements

**Fill in any extra requirements here.**

This repository requires Python >= 3.7.

As well as typical scientific Python packages, dependencies include:

- [convnwb](https://github.com/HSNPipeline/convnwb)
- [combinato](https://github.com/jniediek/combinato)

The full list of dependencies is listed in `requirements.txt`.

## Repository Layout

This repository is set up in the following way:

- `metadata/` contains config files that define metadata fields
- `notebooks/` contains notebooks that demonstrate examples of spike sorting related tasks
- `scripts/` contains stand alone scripts to run processes
- `sort/` inherits from convnwb and contains custom code for pre-processing / sorting data
- `shell/` contains shell scripts that run spike sorting related processes

## Run Procedures

The main procedures involved are detailed through the `notebooks`.

To run processes across sessions / subjects, the files in `shell` and `scripts` can be used.

For a detailed description of how this approach works, and instructions on making
updates, see the [SortTEMPLATE](https://github.com/HSNPipeline/SortTEMPLATE).
