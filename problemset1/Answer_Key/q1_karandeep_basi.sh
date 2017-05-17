#! /bin/bash
find=$1
replace=$2
mkdir replace
cp ./*.txt ./replace
sed -i -e "s/$find/$replace/g" ./replace/*.txt
