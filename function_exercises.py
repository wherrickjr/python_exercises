#1
def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False

#2
def is_vowel(x):
    vowels = 0
    for char in x:
        if char in "aeiouAEIOU":
            vowels = vowels + 1
        else:
            vowels = vowels
    if vowels != 0:
        return True
    else:
        return False

#3
def is_constant(x):
    if is_vowel(x) == True:
        return False
    else:
        return True

#4
def capitalize_if_constant(x):
    vowels = "aeiouAEIOU"
    if x[0] not in vowels:
        return x[0].upper() + x[1:]
    else:
        return x

#5
def calculate_tip(bill, rate):
    while rate < 0 or rate > 1:
        error = "please enter a tip rate between 0 and 1"
        return error
    else:
        tip = bill * rate
    return tip

#6
def apply_discount(price, discount):
    discount_price = price - (price * discount)
    return discount_price

#7
def handle_commas(x):
    new = x.replace(",","")
    return new

#10
def normalize_name(x):
    error = "please enter a valid username"
    stripped = x.strip()
    stripped_and_low = stripped.lower()
    stripped_low_and_underscored = stripped_and_low.replace(" ", "_")
    if stripped_low_and_underscored.isalnum() == True:
        return stripped_low_and_underscored
    else:
        return error
    
    
# 11
def cum_sum(x):
    new_list = []
    j = 0
    for i in x:
        j = j + i
        new_list.append(j)
    return new_list