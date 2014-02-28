#!/bin/sh
# Copy all files of a matching type to a given directory, using unique filenames.
#
SAVEIFS=$IFS
#IFS=$(echo -en "\n\b")
COUNT=0
#OUTPUTROOT=$(dirname $2)
find . -name "$1" -not -path "$2/*" | while read FILE; do
#for FILE in $(find . -name "$1" -not -path "$2/*"); do
	COUNT=0
	BASENAME=$(basename "$FILE")
	NAME=${BASENAME}
	while [ -f "$2/${NAME}" ]; do
		NAME="${BASENAME%.*}_${COUNT}.${BASENAME##*.}"
		COUNT=$((COUNT+1))
	done
	cp -p "${FILE}" "$2/${NAME}"
done
IFS=$SAVEIFS