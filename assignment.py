# 1. Decisions at the Crossroad

# Task 1: Code Correction

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# 2. The Story Brancher
    
# Task 1: Code Correction
    
choice = input("Do you choose the path to the left or right? ")

if choice == "left":
    print("You find a treasure chest!")
elif choice == "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")

# 3. The Greatest Showdown

# Task 1: Identify the Greatest
    
numbers = []
choice = int(input("Enter a number: "))
numbers.append(choice)
choice = int(input("Enter a number: "))
numbers.append(choice)
choice = int(input("Enter a number: "))
numbers.append(choice)
maximum = max(numbers)
minimum = min(numbers)
print("The maximum is ", maximum)

# Task 2: Identify the Smallest
print("The minimum is ", minimum)

# Task 3: Equality Check
from collections import Counter
import datetime
counter = Counter(numbers)

# print(len(counter))

# print(counter)
if numbers[0] == numbers[1] and numbers[0] == numbers[2]:
    print("All numbers are equal")
elif(len(counter)) == 2 and maximum == counter.most_common(1)[0][0]:
    print("Two numbers are equal and the largest")
elif(len(counter)) == 2 and minimum == counter.most_common(1)[0][0]:
    print("Two numbers are equal and the smallest")
else:
    print("All numbers are unique")

# 4. Leap Year Explorer
# Task 1: Leap Year Checker

from datetime import datetime
year_input = int(input("Please enter a year: "))

current_year = datetime.now().year

is_past = False
is_future = False
is_current = False

if current_year < year_input:
    is_future = True
elif current_year > year_input:
    is_past = True
else:
    is_current = True

def leapYearChecker(year, tense):
    if year % 4 != 0:
        print(f"The given year {tense} not a leap year!")
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"The year given {tense} a leap year and is a century year")
            else:
                print(f"The given year {tense} not a leap year and is a century year!")
        else:
            print(f"The year given {tense} a leap year!")


if(is_past):
    leapYearChecker(year_input, "was")
else:
    leapYearChecker(year_input, "is")