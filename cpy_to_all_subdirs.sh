#!/bin/bash
# only if file is given as input para
if [ "$#" -lt 1 ]; then
	echo "pls provide a file to cpy"
	exit 1
fi
# cpy to all
find . -maxdepth 1 -type d -exec cp -v $1 {} \;
