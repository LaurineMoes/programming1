file = open("Kaartnummers.txt", "r")

wit = file.readlines()

for i in wit:
    print("{:1} heeft kaartnummer: {}".format(i.split(",")[0][:-1], i.split(",")[1]))

file.close()

