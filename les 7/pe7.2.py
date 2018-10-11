file = open("Kaartnummers.txt", "r")

wit = file.readlines()

for i in wit:
    print("{:10} heeft kaartnummer: {}".format(i.split(",")[0][:-1], i.split(",")[0]))

file.close()

