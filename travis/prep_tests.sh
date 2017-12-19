#!/bin/bash

set -ev

if [ "$#" -ne 1 ] ; then
    echo "Usage: "$0" <test>"
    exit 1
fi

test="$1"

if [ "$test" = "static" ]; then
    apt install -y python3-pip
    python3 -m pip install -r requirements-devel.txt
elif [ "$test" = "ropa/tests/unit" ]; then
    echo "Currently no unit tests"
else
    echo "Unknown test suite: $test"
    exit 1
fi

./runtests.sh $test
