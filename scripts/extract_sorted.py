"""Extract spike sorting solutions."""

from convnwb.sorting.process import process_combinato_data

# Import local settings
from settings import PATHS, SORT_SETTINGS

###################################################################################################
###################################################################################################

def extract_sorted(paths=PATHS, settings=SORT_SETTINGS):
    """Extract spike times from spike-sorted data."""

    print('\n\nEXTRACTING SPIKE SORTING SOLUTIONS\n\n')

    for chandir in paths.get_subfolders('sorting'):

        print('Processing: ', chandir)
        process_combinato_data(chandir, paths.sorting, settings['polarity'],
                               settings['user'], paths.spikes)

    print('\n\nFINISHED EXTRACTING SPIKE SORTING SOLUTIONS\n\n')

if __name__ == '__main__':
    extract_sorted()
