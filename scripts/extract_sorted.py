"""Extract spike sorting solutions."""

import os

import h5py
import numpy as np

from settings import DB

###################################################################################################
###################################################################################################

def extract_sorted(db=DB):
    """Extract spike times from spike-sorted data."""

    print('\n\nEXTRACTING SPIKE SORTING SOLUTIONS\n\n')

    ind = 0
    for subdir, dirs, files in os.walk(db.split_files):

        for file in files:

            if file == 'sort_cat.h5':

                # Get relevant names
                channel_name = subdir.split('/')[-2]
                parent_directory = '/'.join((subdir.split('/')[:-1]))
                savedir = '/'.join((subdir.split('/')[:-2]))

                # Print out status
                print('Processing: ', channel_name)

                # Extract the sorting results
                sorted_data = h5py.File(os.path.join(subdir, file), 'r')
                sorted_groups = np.array(sorted_data.get('groups'))
                sorted_idx = np.array(sorted_data.get('index'))
                skipped = np.where(np.diff(sorted_idx) > 1)
                clusters = np.unique(sorted_groups[(sorted_groups[:, 1] > 0), 1])

                # Get the spiking results from the raw data
                raw_data = h5py.File(os.path.join(parent_directory, f'data_{channel_name}.h5'), 'r')
                raw_data_neg = raw_data.get('neg')
                spike_waveforms = np.array(raw_data_neg.get('spikes')) * 0.25 # Scale because of Blackrock
                spike_times = np.array(raw_data_neg.get('times'))
                spike_clusters = np.zeros(len(spike_times))

                # Check for channels with no clusters detected in the channel
                if np.size(clusters) < 1:
                    print('  There were no clusters on this channel.')
                    cluster_class = [spike_clusters, spike_times]

                else:

                    print('  Found clusters: extracting spike times.')
                    spike_classes = np.zeros(len(spike_times))

                    # Gets the classes for all the initial spikes detected
                    temp_classes = np.array(sorted_data.get('classes'))
                    valid_classes_clusters = np.squeeze(sorted_groups[np.where(sorted_groups[:, 1] > 0), :])

                    for k in range(len(sorted_idx)):

                        spike_classes[sorted_idx[k]] = temp_classes[k]

                        # If there is only one cluster
                        if valid_classes_clusters.ndim == 1:

                            if spike_classes[sorted_idx[k]] == valid_classes_clusters[0]:
                                spike_clusters[sorted_idx[k]] = valid_classes_clusters[1]

                        else:
                            for ind in range(np.shape(valid_classes_clusters)[0]):
                                if spike_classes[sorted_idx[k]] == valid_classes_clusters[ind, 0]:
                                    spike_clusters[sorted_idx[k]] = valid_classes_clusters[ind, 1]

                    # Get rid of non-sorted 'spikes'
                    if valid_classes_clusters.ndim == 1:
                        spike_waveforms = spike_waveforms[np.in1d(spike_classes, valid_classes_clusters[0]), :]
                        spike_times = spike_times[np.in1d(spike_classes, valid_classes_clusters[0])]
                        spike_clusters = spike_clusters[np.in1d(spike_classes, valid_classes_clusters[0])]
                        spike_classes = spike_classes[np.in1d(spike_classes, valid_classes_clusters[0])]

                    else:
                        spike_waveforms = spike_waveforms[np.in1d(spike_classes, valid_classes_clusters[:, 0]), :]
                        spike_times = spike_times[np.in1d(spike_classes, valid_classes_clusters[:, 0])]
                        spike_clusters = spike_clusters[np.in1d(spike_classes, valid_classes_clusters[:, 0])]
                        spike_classes = spike_classes[np.in1d(spike_classes, valid_classes_clusters[:, 0])]

                    cluster_class = [spike_clusters, spike_times]

                    file_name = f'times_{channel_name}_{str(ind)}.h5'
                    hf = h5py.File(str(db.sorting / file_name), 'w')
                    g1 = hf.create_group('spike_data_sorted')
                    g1.create_dataset('spike_waveforms', data=spike_waveforms)
                    g1.create_dataset('spike_times', data=spike_times)
                    g1.create_dataset('spike_clusters', data=spike_clusters)
                    g1.create_dataset('spike_classes', data=spike_classes)
                    hf.close()

                    ind += 1

                # Print out status
                print('Processing: ', channel_name, ' - ', cluster_msg)

    print('\n\nFINISHED EXTRACTING SPIKE SORTING SOLUTIONS\n\n')

if __name__ == '__main__':
    extract_sorted()
