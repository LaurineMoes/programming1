

def nieuw(oud):
    nieuw = []
    if len(oud) >= 4:
        for words in oud:
            if len(words) > 4:
                nieuw += [words]
        print(nieuw)
    else:
        print("Minimaal 10 strings!")


lijst = eval(input("Geef lijst met minimaal 10 strings: "))
nieuw(lijst)