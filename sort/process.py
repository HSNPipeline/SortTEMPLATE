"""Helper functions for managing / processing channel information."""

from hsntools.objects import Electrodes

###################################################################################################
###################################################################################################

def process_channels(channels, indices, metadata, subject):
    """Process channel names."""

    n_channels = len(channels)
    n_bundles = int(n_channels / 8)

    assert n_channels % 8 == 0, 'Wrong number of channel labels.'

    electrodes = Electrodes(subject)

    for bi in range(n_bundles):

        b_channels = channels[slice(bi*8,bi*8+8)]
        b_indices = indices[slice(bi*8,bi*8+8)]

        cur_chan = b_channels[0]
        for ch in b_channels:
            assert ch[:-1] == cur_chan[:-1], 'Probe names do not align across bundle'
            assert ch[0] == 'm', 'Channel not labelled as a micro'

        # FILL IN BELOW - PROCESSING OF CHANNEL INFORMATION

        # Probe
        probe = ...

        # Hemisphere
        hemi = ...
        hemi = metadata['hemisphere'][hemi] if hemi in metadata['hemisphere'] else 'unknown'

        # Lobe
        lobe = ...
        lobe = metadata['lobe'][lobe] if lobe in metadata['lobe'] else 'unknown'

        # Region
        region = ...
        region = metadata['region'][region] if region in metadata['region'] else 'unknown'

        electrodes.add_bundle(probe, hemi, lobe, region, channels=b_indices)

    return electrodes
