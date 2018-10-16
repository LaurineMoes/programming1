while True:
    s = input("Geef een string van vier letters: ")
    if len(s) == 4:
        print("Inlezen van correcte string: {} is geslaagd".format(s))
        break
    else:
        print("{} heeft {} letters".format(s, len(s)))