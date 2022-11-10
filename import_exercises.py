from function_exercises import calculate_tip
calculate_tip(540,.2) #question 1 answer

import itertools as yo #imports itertoold module

x = list(yo.combinations_with_replacement('abcd123', 8 ))
print(len(x)) # question 2A, this counts the amount of combinations for abcd123

y = list(yo.combinations_with_replacement('abcd',2))
print(len(y)) #shows how many combinations with 2 letters


## what is a permutation?
#question 3
import json
x = json.load(open('profiles.json')) # this stores the json list
#of dictionaries into the variable files

total_users = len(x) #gives total number of dictionaries

def total_active_users(dictionary):
    active_users = []
    for i in dictionary:
        if i["isActive"] == True:
            active_users.append(i)
    return len(active_users)  # function for active users, total = 9

def total_active_users(dictionary):
    active_users = []
    for i in dictionary:
        if i["isActive"] == False:
            active_users.append(i)
    return len(active_users) #gives total for non active users


#total sum of balances

something = [] #this list holds only the balance keys from the dictionary
balances = [] # this holds the balance values without the $
only_dollars = [] # this holds the values without the commas
convert = [] # this holds the converted values 
for i in x:
    balances.append(i["balance"])
for a in balances:
    a = a.strip('$')
    something.append(a)
for b in something:
    b = b.replace(",","")
    only_dollars.append(b)
for c in only_dollars:
    c = float(c)
    convert.append(c)


sum(convert) # adds all float numebers together

#average balance per user:
total_balances = sum(convert) #assigns total balances to variable

average_per_user = total_balances / total_users
print(average_per_user) #gives average balance per user


# fins the user with the lowest balance:
[i for i, d in enumerate(x) if '$1,214.10' in d.values()] 
#this function searches for the minimum balance value with is 1,214.10 and outputs the
# index for the dictionary that has this value, user [6]

# the following code produces the index of the dictionary with the highest value: user [3]

[i for i, d in enumerate(x) if '$1,214.10' in d.values()]

# the below code puts all the favorite fruits from the json file into a list favorite_fruit

favorite_fruit = []

for i in x:
    favorite_fruit.append(i["favoriteFruit"])
    
print(favorite_fruit)

#the following code tells you the amount of each favorite fruit that was listed:
strawberry = 0
apple = 0
banana = 0
for i in favorite_fruit:    
    if i == 'apple':
        apple = apple + 1

for i in favorite_fruit:
    if i == 'strawberry':
        strawberry = strawberry + 1

for i in favorite_fruit:
    if i == 'banana':
        banana = banana + 1
print('strawberry: ' + str(strawberry))
print('apple: ' + str(apple))
print('banana: ', str(banana))
# most common fruit is strawberry and lease common fruit is apple


# code below calculates total number of messages

greetings = [] #holding list for values from dictionary with key "gretting"

for i in x:
    greetings.append(i["greeting"]) #this for loop extracts all the greeting messages from the dictionary


number_of_messages = [] #holding list for numeric values from greetings holding list
messages_int = [] # holding list for casted numbers from number_of_messages
for i in greetings:
    s = ''.join(m for m in i if m.isdigit())
    number_of_messages.append(s) #for loop takes out the numeric values from the string from the greeting
    #key of the dictionary

for y in number_of_messages:
    messages_int.append(float(y)) #this takes the list of numeric strings from numbers_of messages
    # and casts them into float numbers so they can be added.
    
print(sum(messages_int)) # adds all the floats from the messages_int list

