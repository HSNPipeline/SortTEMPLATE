"""Settings for spike sorting recordings."""

from hsntools.paths import Paths

###################################################################################################
###################################################################################################

#### DEFINE SUBJECT INFORMATION

EXPERIMENT = 'XX'
SUBJ = 'XX'
SESSION = 0

SESSION = {
    'SUBJECT' : SUBJECT,
    'EXPERIMENT' : EXPERIMENT,
    'SESSION' : SESSION,
}

#### DEFINE SPIKE SORTING INFORMATION

POLARITY = 'neg'     # 'neg' / 'pos' - sorting polarity
USER = 'XXX'         # for combinato sorting, the 3 character user that is appended to outputs

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

# Collect together spike sorting settings
SORT_SETTINGS = {
    'polarity' : POLARITY,
    'user' : USER,
}
