# Sorting Shell Script

This shell script can be used to run the automatic steps of the Combinato spike sorting.

To run this shell script:
- replace `$POLARITY$` with the polarity (either `pos` or `neg`)
- replace `$USER$` with the user name that will run sorting
    - This should be the first 3 characters (eg user `name.last` should put `nam`)

Note that this shell script runs in the current directory, and so should be
copied into any folder in which one wishes to run automatic spike sorting.
