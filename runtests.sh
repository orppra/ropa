#!/bin/bash

set -e

export PATH=$(pwd)/bin:$PATH
export PYTHONPATH=$(pwd)${PYTHONPATH:+:$PYTHONPATH}

printhelp(){
    echo "Usage: "
    echo "    ./runtests.sh static"
    echo "    ./runtests.sh unit"
}

parseargs(){
    if [[ "$#" -eq 0 ]]; then
        printhelp
	exit 1
    else
        if [ "$1" == "static" ] ; then
            run_static_tests
        else
            run_unit_tests "$@"
        fi
    fi
}

python -m coverage 1>/dev/null 2>&1 && coverage="true"

run_static_tests(){
    SRC_PATHS="ropa"
    python -m flake8 --max-complexity=10 $SRC_PATHS
}

run_unit_tests(){
    if [[ ! -z "$coverage" ]] && [[ "$1" == "unit" ]]; then
        python -m coverage erase
        python -m coverage run --branch --source ropa -m pytest "tests"
    else
        python -m pytest "$1"
    fi
    python -m codecov 1>/dev/null 2>&1
}

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    printhelp
    exit 0
fi

parseargs "$@"

echo -e "\e[1;32mEverything passed\e[0m"
