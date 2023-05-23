#!/bin/bash

files=`ls ./*.hdf5`
for eachfile in $files
do
    css-extract --files $eachfile --h5
done
   
css-mask-artifacts
ls */*.h5 > do_sort.txt
css-prepare-sorting --neg --jobs do_sort.txt
css-cluster --jobs sort_neg_tom.txt --single
css-combine --jobs sort_neg_tom.txt --single