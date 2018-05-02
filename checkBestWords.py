import json
import glob
import operator

h = {}
files = (glob.glob("files/DataJson/*"))

files = sorted(files)

cluster = [4,0,3,5,1,5,2,2,0,6,1,6,4,3,6,5]

final = {}

def print_cluster( id, cluster ):
    print "Cluster: ", id

    row = ""
    counter = 0
    for item in cluster:
        row += item[0] + "\t"
        counter += 1
        if counter == 10:
            print row
            row = ""
            counter = 0
    print row
    print "\n"

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
     print_cluster( h, sorted(final[h].items(), key=operator.itemgetter(1)) )

