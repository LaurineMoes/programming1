cijferICOR = 8
cijferPROG = 5
cijferCSN = 6
gemiddelde = cijferCSN + cijferICOR + cijferPROG / 3
cijfers = cijferICOR + cijferCSN+ cijferPROG
som = sum(cijfers)
ant = som / (len(cijfers))
beloning = som * 30
print('beloning' + str(beloning))

