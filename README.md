# SortTEMPLATE

Template structure for running spike sorting on microwire data.

[![Template](https://img.shields.io/badge/template-HSUPipeline/SortTEMPLATE-yellow.svg)](https://github.com/HSUPipeline/SortTEMPLATE)

## Overview

This repository covers information and guides for running SpikeSorting on single-unit data.

For resources and a list of available spike sorters, see the
[Spike Resources](https://github.com/openlists/SpikeResources#spike-sorting)
open list.

## Repository Layout

This repository is set up in the following way:

- `metadata/` contains config files that define metadata fields
- `notebooks/` contains notebooks that demonstrate examples of spike sorting related tasks
- `scripts/` contains stand alone scripts to run processes
- `shell/` contains shell scripts that run spike sorting related processes

## Notes

Note: perhaps want to move this stuff?

### Sorting with Combinato

[Combinato](https://github.com/jniediek/combinato/)
is a Python tool for spike sorting.

For tutorials and documentation, see the
[Wiki](https://github.com/jniediek/combinato/wiki/).

Combinato is described in
[this paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166598).

### Sorting with SpikeInterface

[SpikeInterface](https://github.com/SpikeInterface/spikeinterface)
is a tool that spike sorting workflows, and allows for running many different spike sorters.

For more information, see the
[documentation](https://spikeinterface.readthedocs.io/en/latest/).

SpikeInterface is described in
[this paper](https://elifesciences.org/articles/61834).

### Core Resources

Papers:
- [Past, present and future of spike sorting techniques](https://www.sciencedirect.com/science/article/pii/S0361923015000684)
- [Quality Metrics to Accompany Spike Sorting of Extracellular Signals](https://www.jneurosci.org/content/31/24/8699.short)

