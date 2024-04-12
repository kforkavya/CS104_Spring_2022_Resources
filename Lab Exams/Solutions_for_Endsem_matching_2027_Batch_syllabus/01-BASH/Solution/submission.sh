#!/bin/bash
count=0
rm -f log.txt 2> /dev/null
touch log.txt
for filepath in $(find $1 -type f -name "*.py")
do
    #We need filename only, "find" command returns entire address of that file
    rm -f $filepath
    filename=$(basename $filepath)
    echo "Deleted "$filename >> log.txt
    count=$(($count + 1))
done
echo $count