"""Split raw data files into channels."""

import h5py

# Add brPY to path
import sys
br_path = '/home1/tom.donoghue/repos/brPY'
sys.path.append(br_path)
from brpylib import NsxFile

# Import settings
from settings import PATHS

###################################################################################################
###################################################################################################

def split_files(data_file):
    """Split raw recording files into single-channel data files."""
    
    print('\n\nLOADING RAW DATA\n\n')

    # Load raw data file
    nsxfile = NsxFile(data_file)
    nsp_data = nsxfile.getdata()
    nsxfile.close()
    
    # Separate data object and params information
    data = nsp_data.pop('data')
    params = nsp_data

    print('\n\nSPLITTING CHANNEL FILES\n\n')
    
    # Split the data by channels and write into hdf5 files
    for ix, electrode in enumerate(params['elec_ids']):
        
        # Skip sync pulse channel
        if electrode == '129':
            continue

        # Optional addition: specifically process channels in the jacksheet
        #if electrode in jacksheet.channel_index:

        print('  splitting electrode file: {}'.format(electrode))

        # Save out HDF5 of microdata        
        file = h5py.File(db.split_files / 'chan_{}.hdf5'.format(electrode), "w")
        file.create_dataset('data', data=data[ix, :], dtype='<i2')
        file.close()
    
if __name__ == '__main__':
    split_files()
