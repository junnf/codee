#!/bin/bash

# _Log=`cat $1`
# echo $_Log
while read line;
do
    echo $line;
    echo "aaa"
done < $1

