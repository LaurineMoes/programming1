def kwadraten_som(grondgetallen):
    kwadraat = 0
    for pos in getallen:
        if pos >= 0:
            kwadraat += (pos ** 2)
    return kwadraat

print (kwadraten_som([4, 5, 3, -81]))