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
files = json.load(open('profiles.json')) # this stores the json list
#of dictionaries into the variable files

len(x) #gives total number of dictionaries

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
