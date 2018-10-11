file = open("Kaartnummers.txt", "r")

list = []

wit = file.read().split("\n")

for i in wit:
    list += [(i.split(",")[0])]

print ("Deze file telt {} regels.\nHet grootste kaartnummer is: {}.\nDit staat op regel {}.".format(len(wit), max(list), list.index(max(list)) + 1))

file.close()