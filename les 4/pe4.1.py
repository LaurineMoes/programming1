cijferICOR = 6
cijferPROG = 7.5
cijferCSN = 7
gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning = (cijferICOR + cijferPROG + cijferCSN) * 30
overzicht = "Mijn cijfers zijn gemiddeld een " + str(gemiddelde)[0:3] + " en het levert mij een beloning van " + str(beloning) + ",- op!"
print (overzicht)