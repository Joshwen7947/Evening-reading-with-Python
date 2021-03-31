# famousQuote = 'Albert Einstein once said "I taught the world that E = MC2"'
# print(famousQuote)
teamPlayers = ['billy','rose','tyson','brad','josh','aaron']
print('Here are the first three players on the team:\n')
for player in teamPlayers[:3]:
    print(player.title())

myFavortieFoods = ['pizza','tacos','chinese','bun dau']
print(myFavortieFoods)
friendsFavoriteFoods = myFavortieFoods[:]
print(friendsFavoriteFoods)

# print('My favorite foods are: ')
# print(myFavortieFoods)
# print('\nMy friends favorite foods are: ')
# print(friendsFavoriteFoods)

myFavortieFoods.append('Cheese Burger')
friendsFavoriteFoods.append('steak')

print('My favorite foods are: ')
print(myFavortieFoods)
print('\nMy friends favorite foods are: ')
print(friendsFavoriteFoods)

# tuple - cant change unlike a list
lovers = ('james','jacky')
print(lovers)

print(lovers[0])



# if statements ~ not, or, and 
cars = ['audi','bmw','aston martin','jaguar','porsche','ferrari']

# 'audi' in cars

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'peppers'
if requested_topping != 'mushrooms':
    print('Hold the mushrooms')


age1 = 21
age2 = 24

if age1 >= 21:
    print('of legal age')
else:
    print('not of age')


if age1 > 10 and age1 < 30:
    print('prime age')
else:
    print('not a good age')

if age1 == 20 or age2 == 24:
    print('Working well')
else:
    print('not working')


banned_users = ['john','jacky','chuck',]
user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, you can post in this group chat')
else:
    print(f'{user.title()}, you are BANNED from posting in group')