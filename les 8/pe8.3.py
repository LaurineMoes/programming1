invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

def getallen(tellen):
    list = (sorted(map(int, tellen.split("-"))))
    print ("Gesorteerde list van ints: {}\nGrootste getal: {} en Kleinste getal:"
           " {}\nAantal getallen: {} en Som van de getallen: {}\nGemiddelde: {}".format(list, max(list)
                    , min(list), len(list), sum(list), sum(list) / len(list)))


(getallen(invoer))