
f = open("PARP.csv", "w")
actives = open("actives_final.ism", "r").readlines()
decoys = open("decoys_final.ism", "r").readlines()

for x in actives:
    f.write("\t{}\t1\n".format(x.split()[0]))
for x in decoys:
    f.write("\t{}\t-1\n".format(x.split()[0]))

f.close()


