#!/bin/bash

# Check if a number is provided as input
if [ $# -eq 0 ]
then
    echo "No number provided. Please provide a number as an argument."
    exit 1
fi

# Store the provided number in a variable
number=$1

mkdir "day-$number"

cd "day-$number"

touch input.txt
echo "if __name__ == \"__main__\":
    lines = [line.strip() for line in list(open(\"./input.txt\"))]" > main.py

echo "Folder 'day-$number' created with files 'input.txt' and 'main.py'"
