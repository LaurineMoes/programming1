def gemiddelde(regel):
    rots = 0
    for i in regel.split(" "):
        rots += len(i)
    return rots / len(regel.split(" "))

print ("De gemiddelde lengte van de woorden in de zin: {:.0f}".format(gemiddelde(input("Typ een willekeurige zin: \n"))))