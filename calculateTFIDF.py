import json
from os import listdir
from os.path import isfile, join
import math

# Set the file path of our cleaned words files
filepath = "Files/Cleaned/"

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

def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"

# Looping every document again to calculate weights
with open('Files/Weighted/totalWeights.csv', 'w') as csv:

    # First line in csv file
    csv.write( u'files,' + u','.join(globalFreqs.keys()).encode('ascii', 'backslashreplace')  )
    csv.write("\n")

    # Every file in the folder
    for filename in onlyfiles:
        data = json.load(open(filepath + filename))

        # Looping every word and getting it's weight
        total_weights = {}
        weight_str = ""
        for key in data:
            tf = data[key]
            df = globalFreqs[key]
            weight = tf *  math.log1p(len(onlyfiles)/df)
            total_weights[key] = weight

        # Checking the weights of the file onto the csv file
        for k in globalFreqs:
            if k in data:
                weight_str += str(total_weights[k]) + ","
            else:
                weight_str += "0,"

        # Write into the csv
        csv.write( filename + "," + weight_str )
        csv.write("\n")

        # Saving files
        with open('Files/Weighted/' + filename, 'w') as outfile:
            json.dump(total_weights, outfile)

