import random as r

test = open("test.csv", "w")
train = open("train.csv", "w")
validate = open("validate.csv", "w")

lines = open("PARP.csv", "r").readlines()
r.shuffle(lines)

train_indice = int(len(lines) * 0.8)
validate_indice = int(len(lines) * 0.9)

for x in lines[:train_indice]:
    test.write(x)

for x in lines[train_indice:validate_indice]:
    train.write(x)

for x in lines[validate_indice:]:
    validate.write(x)





