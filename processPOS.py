import json
import glob

#Import files
files = (glob.glob("files/POS-Freeling/*"))
c = 0
d = {}
#Import Lemma files from Freeling Software
for file in files:
    filename = file[file.rfind("/") + 1:]
    filename_small = filename.replace(".txt", ".json")
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
    with open("files/DataJson/" + filename_small, 'w') as fp:
        json.dump(d, fp, sort_keys=True, indent=4)

print "\n\nDataJson done succesfully"