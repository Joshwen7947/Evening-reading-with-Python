
### Displays all values even repeat values!

print('The following languages have been mentioned:')
for language in languages.values():
    print(language.title())

### Displays all values on once with no repeats!

print('The following languages have been mentioned:\n')
for language in set(languages.values()):
    print(language.title()) 

### Practice for page #105 in python crash course

major_rivers = {
'mekong delta': 'vietnam',
'nile': 'egypt',
'amazon': 'brazil',
'mississippi': 'united states'
}

for river, country in major_rivers.items():
    print(f"The {river.title()} runs through the country of {country.title()}")



languages = {
    'josh': 'python',
    'bob':'c++',
    'dan': 'ruby',
    'joelle': 'c#',
    'peter': 'java',
    'rosa': 'ruby',
    'paolo': 'c#',
    'james': 'python'
}

people_to_take_survey = [
'josh',
'bob',
'dan', 
'joelle',
'peter',
'thai',
'son',
'rosa',
'paolo',
'james',
'brad',
'sean',
]
print(people_to_take_survey)
if people_to_take_survey in languages:
    for people in people_to_take_survey:
        print(f'{people.title()}, thanks for taking the survey!')

 
if name in people_to_take_survey:
    language = languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!\n")
else:
    print(name.title() + 'What is your favorite programming language?')


# pizza test

pizza = {
    'crust':'thick',
    'toppings': ['mushrooms','extra  cheese', 'pepperoni']
}

print(f"You ordered a {pizza['crust']} - crust pizza with the toppings of:")
for topping in pizza['toppings']:
    print('\t'  + topping.title())