import json
from os import listdir
from os.path import isfile, join
import math

# Set the file path of our cleaned words files
filepath = "files/Cleaned/"

# Getting names of all the files in the cleaned folder
onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]

# Setting the global frequencies of all words in all files
globalFreqs = {}

# Loop getting the global frequencies
for filename in onlyfiles:
    data = json.load(open(filepath + filename))

    # Counting in how many documents there is an specific word
    for key in data:
        ############################
        #
        # Your code goes here
        #
        ############################


# Looping every document again to calculate weights
with open('files/Weighted/totalWeights.mat', 'w') as mat:

    # First line in csv file
    mat.write( str(len(onlyfiles)) + " " + str(len(globalFreqs)) )
    mat.write("\n")

    # Every file in the folder
    for filename in onlyfiles:
        data = json.load(open(filepath + filename))

        # Looping every word and getting it's weight
        total_weights = {}
        weight_str = ""
        for key in data:
            ############################
            #
            # Your code goes here
            #
            ############################

        # Checking the weights of the file onto the csv file
        for k in globalFreqs:
            if k in data:
                weight_str += str(total_weights[k]) + "\t"
            else:
                weight_str += "0\t"

        # Write into the mat file
        mat.write( weight_str )
        mat.write("\n")

