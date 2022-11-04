#1
def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False

#2
def is_vowel(x):
    for letter in x:
        if letter in "aeiouAEIOU":
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
def calculate_tip(bill):
    tip = bill * 0.2
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
    stripped = x.strip()
    stripped_and_low = stripped.lower()
    stripped_low_and_underscored = stripped_and_low.replace(" ", "_")
    return stripped_low_and_underscored