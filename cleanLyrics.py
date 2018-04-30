import json
import glob

#Import files
files = (glob.glob("files/Lyrics/*"))

#Initialize banned words.
banned_words = {
    "yeah": 1,
    "oh": 1
}

#Clean all words from all files
for file in files:
    filename = file[file.rfind("/") + 1:]
    with open(file, 'r') as f:
        write = ""
        for line in f:
            words = map(str, line.strip().split(' '))
            for w in words:
                if w not in banned_words.keys():
                    if len(w) > 2:
                        write += w + " "
        write += '\n'
    with open("files/Lemma/"+ filename, 'w') as l:
        l.write(write)
print "\n\nLemma done succesfully."


