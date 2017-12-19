#!/bin/bash

set -ev

if [ "$#" -ne 1 ] ; then
    echo "Usage: "$0" <test>"
    exit 1
fi

test="$1"

if [ "$test" = "static" ]; then
    sudo apt install -y python3-pip
    sudo python3 -m pip install -r requirements-devel.txt
elif [ "$test" = "ropa/tests/unit" ]; then
    sudo apt install -y python3-pip
    sudo python3 -m pip install -r requirements-devel.txt -r requirements.txt
else
    echo "Unknown test suite: $test"
    exit 1
fi

./runtests.sh $test
