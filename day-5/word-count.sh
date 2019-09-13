#!/bin/bash

for file in *.py
do
    # echo -n "$file "
    newName=$(echo $file | sed -e 's/\.py$/.wc/')

    if [ -f $newName ]
    then
        echo "New name $newName already exists!!!!"
        exit 1
    fi

    wc -w < $file > $newName
done
