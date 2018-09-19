name = input('What is your name:')
age = int(input('What is your age:'))

if age >= 18:
    print('Your allowed to vote')
else:
    print('wait a little longer to vote'+ ( name))