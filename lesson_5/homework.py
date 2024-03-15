# Homework Lesson 5 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Make a number Positive
#
# Create a variable called my_number and set it to any integer value.
# Write code to make the number positive if it's negative, and keep it
# as is if it's already positive or zero.
#
# Example:
# Input: -3 => Output: 3
# Input: 5 => Output: 5
my_number = int(input("Enter your number: "))
if my_number < 0:
    print(my_number * -1)
else:
    print(my_number)

# ---------------------------------------------------------------------

# Challenge 2
# BinGo!
#
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”
# Otherwise, print the original number: “{number} is just a number”
number = float(input("Enter your number: "))
if number % 3==0 and number %7==0:
    print("BinGo")
elif number % 3 ==0:
    print("Bin")
elif number % 7 ==0:
    print("Go")
else:
    print(f"{number} is just a number")

# ---------------------------------------------------------------------

# Challenge 3
# Find the middle number
#
# Given three different numbers x, y, and z, find the number that is neither
# the smallest nor the largest and print it.
#
# Example:
# x = 1, y = 5, z = 3 => Output: 3
x = int(input("Enter X: "))
y = int(input("Enter Y: "))
z = int(input("Enter Z: "))
if y < x < z or z < x < y:
    print(f"{x}")
elif x < y < z or z < y < x:
    print(f"{y}")
elif x < z < y or y < z < x:
    print("z")
else:
    print("some numbers are equal")


# ---------------------------------------------------------------------

# Challenge 4
# Palindrome Numbers
#
# Ask a user to input a number.
# Write a program to check if the given number is a palindrome.
# It should print True if the number is a palindrome and False if it is not.
#
# Palindrome number: 121, 898
entered_number = int(input("Enter your number: "))
number = str(entered_number)

if number[0]==number[-1]:
    print("TRUE")
else:
    print("FALSE")

# ---------------------------------------------------------------------

# Challenge 5
# Reverse a string
#
# You're part of a team working on analyzing customer reviews for a new video game.
# Due to a software glitch, some reviews have been recorded in reverse with punctuation
# at the beginning instead of the end. Your task is to correct these reviews so that they
# are in the correct order and the punctuation is appropriately placed at the end of the
# sentence or word.
#
# Example: "tcefreP!" -> Perfect!

entered_review = input("Enter wrong review: ")
review = str(entered_review)
right_review = review [: : -1]

print(f"{right_review}")