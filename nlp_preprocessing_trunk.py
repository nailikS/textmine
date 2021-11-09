import sys
import os
import re
import string
import csv
import spacy
from nltk.stem import PorterStemmer

class lecture:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.processedDesc = []

def readFirstLine(line):
    i = 0
    indexID = -1
    indexTitle = -1
    indexDesc= -1
    for elem in line:
        if elem == 'ID':
            indexID = i
        elif elem == 'Title':
            indexTitle = i
        elif elem == 'Description':
            indexDesc = i
        i += 1
    return (indexID, indexTitle, indexDesc)
    
def readLectures(input):
    dataset = []
    indexID = -1
    indexTitle = -1
    indexDescription = -1
    i = 0
    lines = csv.reader(input, delimiter='\t')
    for line in lines:
        if (i == 0):
            (indexID, indexTitle, indexDescription) = readFirstLine(line)
            i = i+1
        else:
            dataset.append(lecture(line[indexID], line[indexTitle], line[indexDescription]))
    return dataset

if len(sys.argv) != 2:
    print ("Usage: inputdata.csv")
else:
    print ("Processing input...")
    input = open(str(sys.argv[1]), 'r')
    #array of lectures
    dataset = readLectures(input)
    input.close
    print(len(dataset))