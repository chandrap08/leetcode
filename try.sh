#!/bin/bash
input='abc.log'
while IFS= read line
do
    echo "$line"
done < $input