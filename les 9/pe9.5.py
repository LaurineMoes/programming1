namen = {}
count = 0
name = input('geef een naam: ')
while name != '':

    if namen.get(name):
        namen[name] = namen[name]+1
    else:
        namen[name] = 1
    count = count + 1
    name = input('geef nog een naam: ')
for name in namen:
    if namen[name] >=2:
        print('er zijn',str(namen[name]),'studenten met de naam',str(name))
    else:
        print('er is 1 student met de naam',str(name))