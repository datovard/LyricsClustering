import json
import glob

#Import files
files = (glob.glob("Lyrics/*"))

#Initialize banned words.
banned_words = {
    "yeah": 1,
    "oh": 1
}

#Clean all words from all files
for file in files:
    path, file_name = file.split('/')
    with open(file, 'r') as f:
        write = ""
        for line in f:
            words = map(str, line.strip().split(' '))
            for w in words:
                if w not in banned_words.keys():
                    if len(w) > 2:
                        write += w + " "
        write += '\n'
    with open("Lemma/"+file_name, 'w') as l:
        l.write(write)
print "\n\nLemma done succesfully."


#Import files
files = (glob.glob("POS-Freeling/*"))
c = 0
d = {}
#Import Lemma files from Freeling Software
for file in files:
    path, file_name = file.split('/')
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if(c % 3 == 1):
                if line in d:
                    d[line] += 1
                else:
                    d[line] = 1
            c += 1
    #Export data to json
    with open("DataJson/" + file_name + ".json", 'w') as fp:
        json.dump(d, fp, sort_keys=True, indent=4)

print "\n\nDataJson done succesfully"