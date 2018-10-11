def standaardprijs(afstandKM):
    if afstandKM < 0:
        return 0
    elif afstandKM >= 50:
        bedrag = 0.6 * afstandKM + 15
        return bedrag
    else:
        bedrag = (0.8 * (afstandKM))
        return bedrag

def bepaal_weekend (dag):
    if 7 >= dag >= 5:
        return True
    else:
        return False

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if  12 >= leeftijd <= 65:
        if bepaal_weekend(weekendrit) == True:
            korting = 0.35
            print("U heeft 35% korting")
        else:
            korting = 0.3
            print ("U heeft 30% korting")
    else:
        if bepaal_weekend(weekendrit) == True:
            korting = 0.4
            print("U heeft 40% korting")
        else:
            korting = 0.0
            print("U heeft 0% korting")
    bedrag = (1 - korting) * prijs

    return bedrag

afstandKM = float(input("Hoeveel heb je reisd:"))
weekend= int(input("Hoeveelste dag van de week:"))
leeftijd= int(input("Wat is u leeftijd:"))
print ("U betaalt {:.2f} voor u reis".format(ritprijs(leeftijd, weekend, afstandKM)))
