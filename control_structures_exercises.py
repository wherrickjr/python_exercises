day = input("Enter the day of the week: ")
if day.strip().lower() == 'monday':
    print('it\'s Monday!')
else:
    print('the week is chugging along!')

## 1b

day = 'Tuesday'
print('enter day of the week:')
if (day == 'Saturday' or day == 'Sunday'):
    print('it\'s a weekend')
else:
    print('it\'s a weekday')


## 1c function that calculates paycheck includign overtime pay

hours_worked = int(input("please enter hours worked: "))
hourly_rate = int(input("please enter hourly rate: "))

if hours_worked > 40:
    paycheck_amount = (40 * hourly_rate) + ((hours_worked -40) * 1.5 * hourly_rate )
    print(paycheck_amount)
else: 
    paycheck_amount = hours_worked * hourly_rate
    print(paycheck_amount)

# Loop Basics
#2a
i = 5
while i <= 15:
    print(i)
    i += 1
i = 0
while i <= 100:
    print(i)
    i += 2
i = 100
while -10 <= i <= 100:
    print(i)
    i -= 5

i = 2
while i <= 1000000:
    print(i)
    i = i **2

i = 100
while 5 <= i <= 100:
    print(i)
    i -= 5
#2b For loops

#part i
i = int(input('please enter a number: '))
for n in range(1,11):
    line = n * i
    print(f"{i} * {n} = " + str(line))

#part ii.
for n in range(1,10):
    print(str(n)*n)

#2c part i.

positive = int(input("enter positive integer: "))
while positive < 0:
    positive = int(input("enter positive integer: "))
for n in range(0, positive):
    print(positive)
    positive = positive - 1
        


#part ii.
number = int(input("enter a positive number: "))
i = 0

for n in range(0, number + 1):
    print(i)
    i +=1

# 2c part iii.
odd = 1
positive = int(input("number to skip is: "))
while positive % 2 == 0:
    print("please enter an odd number")
    positive = int(input("number to skip is: "))
for n in range(0, 50):
    if n == positive:
        print("Yikes! Skipping number: " + str(positive))
    elif n % 2 == 1:
        print("Here is an odd number: " +str(n))


#3 FizzBuzz question
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

#question 4
m = 0
squared = int(input("What number would you like to go up to? "))
print("Here is your table!\n")

print("number | squared | cubed")
print("------ | ------- | -----")
for n in range(0, squared + 1):
    print(str(m) + "      |" + str(m ** 2) + "        |" + str(m ** 3))
    m += 1


# 5
while True:
    your_num = int(input("Input your grade here: "))

    if your_num >= 88:
        print("A")
    elif your_num >= 80:
        print("B")
    elif your_num >= 67:
        print("C")
    elif your_num > 60:
        print("D")
    else:
        print("F")
    your_input = input("Do you want to continue? y/n")

    if your_input.lower().strip() == "n":

        break


#6
books_read = [{"title": "Harry potter", "author": "J.K. Roweling", "genre": "fantasy"},
             {"title": "lord of the rings", "author": "J.R. Tolkein", "genre":"fantasy"},
             {"title": "it", "author": "stephen king", "genre": "something else"}]

query = input("enter a genre ")
for book in books_read:
    if book["genre"] == query:
        print(f" {book['title']} is one")



