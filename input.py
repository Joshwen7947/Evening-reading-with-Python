message = input('Please enter your name: ')
print(f'Hello, {message.title()}!')

prompt = 'If you tell me your name, I can personalize this for you.'
prompt += '\nWhat is your name? '
name = input(prompt)
print(f'Hello, {name.title()}!')


age = input('How old are you? ')
age = int(age)
if age >= 21:
    print('You are of drinking age')
else:
    print('Sorry, you can not drink')

    
## Modulo numbers and inputs
number = input('Tell me a number and I will tell you if it is even or odd ')
number = int(number)

if number % 2 == 0:
    print(f'\t{number} is an even number')
else:
    print(f'\t{number} is an odd number')

## RENTAL CAR practice
rental = input('What car would you like? ')
print(f"Let me see if I can find a {rental.title()} for you!")

## Restaurant seating practice
numberOfPeople = input('How many people will be coming? ')
number = int(numberOfPeople)

if number > 8:
    print("You'll have to wait for a table")
else:
    print('We have a table for you now')

### Multiples of ten
number = input('Please input a number to see if it is a multiple of ten: ')
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of ten!")
else:
    print(f"sorry, {number} is not a multiple of ten")