#!/bin/bash

set -ev

if [ "$#" -ne 1 ] ; then
    echo "Usage: "$0" <test>"
    exit 1
fi

test="$1"

if [ "$test" = "static" ]; then
    sudo apt install -y python-pip
    sudo python -m pip install -r requirements-devel.txt
elif [ "$test" = "unit" ]; then
    travis/build_dependencies.sh
    sudo apt install -y python-pip cmake
    sudo python -m pip install -r requirements-devel.txt -r requirements.txt
else
    echo "Unknown test suite: $test"
    exit 1
fi

./runtests.sh $test
