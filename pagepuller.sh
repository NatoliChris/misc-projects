#!/bin/bash

if [[ -z "$1" ]]; then
    echo ""
    echo "usage: $0 <URL>"
    exit
fi

wget --recursive --no-parent --page-requisites --convert-links $1
