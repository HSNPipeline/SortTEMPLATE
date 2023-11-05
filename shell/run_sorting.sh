#!/bin/bash

files=`ls ./*.hdf5`
for eachfile in $files
do
    css-extract --files $eachfile --h5
done

css-mask-artifacts
ls */*.h5 > do_sort.txt
css-prepare-sorting --$POLARITY$ --jobs do_sort.txt
css-cluster --jobs sort_neg_$USER$.txt --single
css-combine --jobs sort_neg_$USER$.txt --single