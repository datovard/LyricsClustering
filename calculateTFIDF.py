import json
from os import listdir
from os.path import isfile, join
import math

# Set the file path of our cleaned words files
filepath = "C:/Users/abad_/Downloads/Data Mining/Limpiadas/"

# Getting names of all the files in the cleaned folder
onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]

# Setting the global frequencies of all words in all files
globalFreqs = {}

# Loop getting the global frequencies
for filename in onlyfiles:
    data = json.load(open(filepath + filename))

    # Counting in how many documents there is an specific word
    for key in data:
        if key not in globalFreqs:
            globalFreqs[key] = 1
        else:
            globalFreqs[key] += 1

# Looping every document again to calculate weights
for filename in onlyfiles:
    data = json.load(open(filepath + filename))

    # Looping every word and getting it's weight
    total_weights = {}
    for key in data:
        tf = data[key]
        df = globalFreqs[key]
        weight = tf *  math.log1p(len(onlyfiles)/df)
        total_weights[key] = weight

    # Saving files
    with open('C:/Users/abad_/Downloads/Data Mining/Pesadas/' + filename, 'w') as outfile:
        json.dump(total_weights, outfile)