import nltk
from nltk.corpus import stopwords
import json
from os import listdir
from os.path import isfile, join

# Getting stopwords from nltk
stop_words = set( stopwords.words('spanish') )

# File path of processed words
filepath = 'Files/DataJson/'

# Getting names of all the files in the lemma folder
onlyfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]

# Looping all files in folder
for filename in onlyfiles:

    # Get the words of the file
    data = json.load( open(filepath + filename) )
    word_tokens = data.keys()

    # Cutting the stopwords from the words array
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    # Creating a new file to save the new json with the original frequencies
    new_dict = {}
    for key in filtered_sentence:
        new_dict[key] = data[key]

    # Saving the file
    with open('Files/Cleaned/' + filename, 'w') as outfile:
        json.dump(new_dict, outfile)