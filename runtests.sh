#!/bin/bash

set -e

export PATH=$(pwd)/bin:$PATH
export PYTHONPATH=$(pwd)${PYTHONPATH:+:$PYTHONPATH}

printhelp(){
    echo "Usage: "
    echo "    ./runtests.sh static"
    echo "    ./runtests.sh ropa/tests/unit"
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

python3 -m coverage 1>/dev/null 2>&1 && coverage="true"

run_static_tests(){
    SRC_PATHS="ropa"
    python3 -m flake8 --max-complexity=10 $SRC_PATHS
}

run_unit_tests(){
    if [[ ! -z "$coverage" ]] && [[ "$1" == "ropa/tests/unit"* ]]; then
        python3 -m coverage erase
        python3 -m coverage run --branch --source ropa -m unittest discover -b -v -s "$1" -t .
    else
        python3 -m unittest discover -b -v -s "$1" -t .
    fi
}

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    printhelp
    exit 0
fi

parseargs "$@"

if [[ ! -z "$coverage" ]] && [[ "$1" == "ropa/tests/unit"* ]]; then
    python3 -m coverage report

    echo
    echo "Run 'python3-coverage html' to get a nice report"
    echo "View it by running 'x-www-browser htmlcov'"
    echo
fi

echo -e "\e[1;32mEverything passed\e[0m"
