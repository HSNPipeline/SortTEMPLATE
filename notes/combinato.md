# Combinato 

Notes on using the Combinato spike sorter. 

## Automatic Processing Notes

- Event detecting requires a detection polarity (positive or negative)
    - Only one polarity can be run at a time
    - BlackRock & Ripple: typically always negative polarity
    - Neuralynx: uses positive polarity
- By default, Combinato defaults to 2 rounds of template matching, but this can be changed to do more

## GUI Notes

GUI Actions:
- To select a cluster press 'enter'
  - This highlights the selected cluster across the visualizations
- To mark a cluster as bad click 'A' for artifact
  - This moves a cluster to the 'Artifacts' group
- To move a cluster, in "AllGroups" click (select) a cluster, and then click the new location to move it to
- To merge a cluster to an existing other cluster:
    - from "All Groups", click on cluster to move and then click an existing cluster to move it to
- To separate out a cluster to a new (empty) cluster:
    - click on Actions / New Group to create a new (empty) cluster
    - From "All Groups", click on the cluster to split out, then to the new (empty) group to move it there

GUI Notes:
- The GUI has 3 categories of clusters: artifacts, unassigned, assigned clusters
- The cluster colors:
    - dark blue: events from the first template matching
    - light blue: events from the second template matching
    - orange: spikes matched to the cluster

Curation Notes:
- For ISIs, ideally want less than ~3% of spikes within 3 ms
