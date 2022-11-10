#1 function determines if a value is an integer or string 2
def is_two(x):
    if x == 2 or x == '2':
        # states if x is either 2 an integer or 2 a string, returns true if it meets this condition
        return True
    else:
        #returns false if statement above is not met.
        return False

#2 # checks to see if a string contains a vowel
def is_vowel(x):
    vowels = 0
    #creates a variable vowels to help determine if there is a vowel in string
    for char in x:
        if char in "aeiouAEIOU":
            vowels = vowels + 1
            #above statement goes through each value in string and 
            #detects if it is in the list of vowels string. If it is, the variable vowels 
            # gets plus 1
        else:
            vowels = vowels
            #if no vowels in input, the vowel variable stays the same
    if vowels != 0:
        return True
        # if there are vowles in the input, vowels would not be equal to 1 therefore, 
        # the function returns True
    else:
        return False
        #if vowels is still 0, then we know there are no vowels

#3 Function detects if a given letter is a constant
def is_constant(x):
    if is_vowel(x) == True:
        return False
    else:
        return True
#if the letter is a vowel, then it is not a constant. So, using the previous function
# that detects a vowel, if it is Ture, then this function would be False and vice versa

#4
def capitalize_if_constant(x):
    vowels = "aeiouAEIOU"
    if x[0] not in vowels:
        return x[0].upper() + x[1:]
        # checks to see if first letter in string is a vowel and then
        #capitalizes it and adds the rest of the string
    else:
        return x
    #if the string doesnt start with a vowel, it just returns the 
    #original string with nothing added

#5
def calculate_tip(bill, rate):
    while rate < 0 or rate > 1:
        error = "please enter a tip rate between 0 and 1"
        return error
        #checks to make sure 'rate' is in valid range (between 0 and 1)
    else:
        tip = bill * rate
        #this is the formaula for calculating the range
    return tip

#6
def apply_discount(price, discount):
    discount_price = price - (price * discount)
    return discount_price
    #this is pretty self explanitory

#7
def handle_commas(x):
    new = x.replace(",","")
    return new
    #inputs a string and replaces commas with nothing


#8 returns letter grade for given score as input
def get_letter_grade(score):
    if(score < 60):
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    elif score < 101:
        return "A"

#9 takes input and removesa all vowles from string
def remove_vowel(string):
    vowel = ('a','e','i', 'o', 'u')
    for x in string.lower():
        if x in vowel:
            string = string.replace(x, "")
        print(string)

#10
def normalize_name(x):
    error = "please enter a valid username"
    #variable to return if an invalid character is entered
    stripped = x.strip()
    #this strips the string of space before and after words
    stripped_and_low = stripped.lower()
    #this makes all the letters in the stripped string lowercase
    stripped_low_and_underscored = stripped_and_low.replace(" ", "_")
    #this takes the spaces between words and replaces them with an underscore
    if stripped_low_and_underscored.isalnum() == True:
        ''' this checks to see if all the characters are alphanumeric'''
        return stripped_low_and_underscored
    else:
        return error
# this makes the user reenter a valid thing.
    
    
# 11
def cum_sum(x):
    new_list = []
    #place holder list
    j = 0
    #starting value that will be added to each term
    for i in x: #for loop is used because it is going to go through each value, one at a time

        j = j + i
        #first, it takes the first value(i), and adds j to it, first, j = 0, and then after
        #the next value (i) is added to it, j becomes a new number.
        #that number is then added to the next value in the list (i).
        new_list.append(j)
        #this adds each value to the place holder list new_lsit
    return new_list

    