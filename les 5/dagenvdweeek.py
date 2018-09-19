dagen = ['maandag', 'dinsdag', 'woensdag']
for dag in dagen:
    afkorting = dag[0:2]
    print(afkorting)


lijst = range(12)
for getal in lijst:
    mod = getal % 2
    if mod == 0:
        print(getal)
