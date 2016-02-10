#!/bin/bash

alert() {
    if [ "$1" -ne 0 ]
    then
        echo "warning"
    else
        echo "fuck"
    fi
}
a=2
alert($a)


