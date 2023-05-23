"""Settings for spike sorting recordings."""

from convnwb.paths import Paths

###################################################################################################
###################################################################################################

#### DEFINE SUBJECT INFORMATION

EXPERIMENT = 'XX'
SUBJ = 'XX'
SESSION = 0

###################################################################################################
## For standard usage, nothing should need to be updated below

# Site related information

SITE_DICT = {}
SITE = SITE_DICT[SUBJ[0]]

## Paths

# Define base & project path
BASE_PATH = '/data12/jacobs_lab/'
PROJECT = 'XX'
PROJECT_PATH = BASE_PATH + PROJECT

# Create the paths object
PATHS = Paths(PROJECT_PATH, SUBJECT, EXPERIMENT, SESSION)
