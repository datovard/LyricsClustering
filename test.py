import json
import glob
import operator

h = {}
files = (glob.glob("files/DataJson/*"))

cluster = [0,5,6,5,5,3,2,4,6,6,4,1,1,0,2,3]

final = {}

counter = 0
for file in files:
    h = json.load(open(file))
    sorted_h = sorted(h.items(), key=operator.itemgetter(1))
    x = sorted_h[-30:-1]
    for w,v in x:
        if cluster[counter] not in final:
            final[cluster[counter]] = {}
        else:
            if w not in final[cluster[counter]]:
                final[cluster[counter]][w] = 1
            else:
                final[cluster[counter]][w] += 1
    counter+=1

for h in final:
    print h, sorted(final[h].items(), key=operator.itemgetter(1))


