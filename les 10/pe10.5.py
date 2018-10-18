def inlezen_beginstation(stations):
    while True:
        beginstation=input("Wat is je beginstation?")
        if beginstation in stations:
            return beginstation
            break
        else:
            print("Deze trein komt niet in {}\n".format(beginstation))

def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation=input("Wat is je eindstation?")
        if eindstation in stations:
            if stations.index(eindstation) > stations.index(beginstation):
                 return eindstation
                 break
            elif eindstation == beginstation:
                 print("Je stapt al in op station {}\n".format(eindstation))
            else:
                 print("Dit station is vóór het station: {}\n".format(beginstation))
        else:
            print("Deze trein komt niet in {}".format(eindstation))

def omroepen_reis(stations, beginstation, eindstation):
    print("Het beginstation {} is het {} station in het traject.".format(beginstation, stations.index(beginstation) + 1))
    print("Het eindstation {} is het {} station in het traject.".format(eindstation, stations.index(eindstation)+ 1))
    print("De afstand bedraagt {} station(s)".format(stations.index(eindstation) - stations.index(beginstation)))
    print("De prijs van het kaartje is {} euro.". format((stations.index(eindstation) - stations.index(beginstation)) * 5))
    print("Jij stapt in de trein in: {}".format(beginstation))
    for i in range(stations.index(beginstation) + 1, stations.index(eindstation)):
        print(" - {}".format(stations[i]))
    print("Jij stapt uit de trein in:{}".format(eindstation))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar','Castricum','Zaandam','Amsterdam' 'Sloterdijk','Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch','Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht' ]

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
