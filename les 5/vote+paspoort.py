age = int(input('Give your age:'))
paspoort = input('Nederland paspoort?')

if age >= 18 and paspoort == "ja":
    print('je mag stemmen.')
else:
    print('Je mag niet stemmen.')

