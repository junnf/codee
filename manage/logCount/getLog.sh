#!/bin/bash

# _Log=`cat $1`
# echo $_Log
while read line;
do
    echo $line;
done < $1

