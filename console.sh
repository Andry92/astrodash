#!/bin/bash
for ((i=1; i<=10; i++))
do
    echo "iterazione $i"
    python extract_random_data.py "$i"
    python astrodash_program.py "$i"
done
