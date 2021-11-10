import sys
import re

__author__ = "Kilian Straka"
__date__ = "10.11.2021"

input = open(str(sys.argv[1]), 'r')

d = dict()

for line in input:
    line = line.strip()
    words = line.split(" ")

    for word in words:
        # Check if the word is already in dictionary
        if bool(re.match('^[a-zA-Z]{2,20}(?:_[a-zA-Z]+)*$', word)):
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

for key in list(d.keys()):
    print(d[key], ":\t", key)
