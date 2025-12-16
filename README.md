# PrepTEMPLATE

Template structure for pre-processing HSN data.

[![Template](https://img.shields.io/badge/template-HSNPipeline/PrepTEMPLATE-yellow.svg)](https://github.com/HSNPipeline/PrepTEMPLATE)
[![Convert](https://img.shields.io/badge/data-ConvertTEMPLATE-lightgrey)](https://github.com/HSNPipeline/ConvertTEMPLATE)
[![Analysis](https://img.shields.io/badge/analysis-AnalyzeTEMPLATE-lightgrey)](https://github.com/HSNPipeline/AnalyzeTEMPLATE)

## TEMPLATE DESCRIPTION

This is a template repository for pre-processing human single-neuron data, including spike sorting.

This template follows the general purpose
[ProjectTemplate](https://github.com/structuredscience/ProjectTemplate)
layout from
[StructuredScience](https://github.com/structuredscience/).

For information on how to use this template in a project, see the
[HSNPipeline Guide](https://github.com/HSNPipeline/Overview/blob/main/Guide.md).

This template includes spike sorting, with the default approach using the
[combinato](https://github.com/jniediek/combinato) spike sorter.

Note: if copying this template for use, this section can be removed.

## Overview

*Provide an overview of the project / data here, for example:*

This repository manages pre-processing for the `XX` task / project.

## Requirements

This repository requires Python >= 3.7.

As well as typical scientific Python packages, dependencies include:

- [hsntools](https://github.com/HSNPipeline/hsntools)
- [combinato](https://github.com/HSNPipeline/combinato)*

The full list of dependencies is listed in `requirements.txt`.

Note that the above link for combinato is for an updated version adapted for us
with the HSNPipeline. The original version is
[here](https://github.com/jniediek/combinato).

*Fill in or edit any additional requirements here.*

## Repository Layout

This repository is set up in the following way:

- `metadata/` contains config files that define metadata fields
- `notebooks/` contains notebooks that demonstrate examples of pre-processing and spike sorting
- `prep/` contains custom code for pre-processing data and running sorting data
- `scripts/` contains stand alone scripts to run processes
- `shell/` contains shell scripts that run pre-processing related operations

*Add or edit any details about repository layout here.*

## Run Procedures

The main procedures involved are detailed through the `notebooks`.

To run processes across sessions / subjects, the files in `shell` and `scripts` can be used.

For a detailed description of how this approach works, and instructions on making
updates, see the [PrepTEMPLATE](https://github.com/HSNPipeline/PrepTEMPLATE).
