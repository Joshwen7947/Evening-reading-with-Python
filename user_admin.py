# Hello Admins:
users = ['admin','josh','thao','gary','bert']
for user in users:
    if user == 'admin':
        print('Hello Admin, Would you like to see a status report?\n')
    else:
        print(f'Hello {user.title()}, Thank you for logging in again\n')

users = []
if users:
    for user in users:
        if user == 'admin':
            print('Hello Admin, Would you like to see a status report?\n')
else:
    print('We need some users\n')

current_users = ['danny','billy','jose','rosa','marie','chuck','Danny','Billy','Jose','Rosa','Marie','Chuck']
new_users = ['shane','aaron','billy','marie','batman','superman',]


for user in new_users:
    if user in current_users:
        print(f'Sorry {user.title()}, this username is already taken.  Choose a new one!\n')
    else:
        print(f'Welcome {user.title()}, You have created an account!  Let us get started\n')

ordinalNumbers = list(range(1,10))
# print(ordinalNumbers)
for number in ordinalNumbers:
    if number == 1:
        print('1st\n')
    elif number == 2:
        print('2nd\n')
    elif number == 3:
        print('3rd\n')
    else:
        print(f'{number}th\n')