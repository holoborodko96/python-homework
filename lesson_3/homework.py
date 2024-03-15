# Homework Lesson 2 - Strings

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# ---------------------------------------------------------------------
# Exercise 1: Personalized Greeting
# Write a program that takes a user's name as input
# and then greets them using an f-string: "Hello, [name]!"
#
# Example Input: "Alice"
# Example Output: "Hello, Alice!"
name = input("Enter yor name: ")
print(f"Hello, {name}!")

# ---------------------------------------------------------------------
# Exercise 2: Greeting with User's Favorite Activity
# Write a program that takes a user's name and their
# favorite activity as input, and then greets them
# using the formatting method of your choice as:
# "Hello, [name]! Enjoy [activity]!"

# Example Input:
# Name: Emily
# Favorite Activity: hiking
# Example Output: "Hello, Emily! Enjoy hiking!"
name = input('Enter your name: ')
fav_activity = input('Enter your favourite activity: ')
print(f'Hello, {name}! Enjoy {fav_activity}!')

# ---------------------------------------------------------------------
# Exercise 3: Membership Cards
# You are designing a simple registration system for a club.
# When new members sign up, you want to ensure their names
# are displayed in uppercase on their membership cards.
# Write a program that takes the new member's name as
# input and prints it in uppercase and prints a welcome message
# using .format()

# Example Input:
# Name: Emily
# Example Output: "Welcome, Emily! Your name in uppercase is: EMILY!"

name = str(input('Enter your name: '))

print('Welcome, {}! Your name in the uppercase is: {}!'.format(name, name.upper()))


# ---------------------------------------------------------------------
# Exercise 4: User Profile Creation
# Build a user profile generator. Ask
# the user for their first name, last name, and age. Create
# a profile summary using .title(), .upper(), and .format().
#
# Example Input:
# First name: john
# Last name: smith
# Age: 28
#
# Example Output:
# Name: John Smith
# Age: 28

first_name = str(input('Enter your first name: '))
last_name = str(input('Enter your last name: '))
age = str(input('Enter your age: '))
print('Name: {} {} \n Age: {}'.format(first_name.title(), last_name.title(), age.upper()))

# ---------------------------------------------------------------------
# Exercise 5: Text message limits
# You are developing a text messaging application that limits the
# number of characters in a single message. Your task is to create
# a Python program that takes a message as input from the user.
# The program should calculate and display the number of characters
# in the message, including spaces, and format the output using
# an f-string. This character count will help users ensure their
# messages fit within the allowed limit.
message = str(input('Enter your message: '))

print(f'The number of symbols in the message is: {len(message)}')


# ---------------------------------------------------------------------
# Exercise 6: Text Transformation Game
# Create a text transformation game. Ask the user
# to enter a sentence. Replace all vowels with '*'. Display the
# modified sentence.
#
# Example Input: "Hello, world!"
# Example Output: "H*ll*, w*rld!"
sentence = input("Enter a sentence: ")
transformed_sentence = sentence.replace('a', '*')
transformed_sentence = transformed_sentence.replace('e', '*')
transformed_sentence = transformed_sentence.replace('i', '*')
transformed_sentence = transformed_sentence.replace('o', '*')
transformed_sentence = transformed_sentence.replace('u', '*')
transformed_sentence = transformed_sentence.replace('y', '*')
print(transformed_sentence)
# ------------------------------# ---------------------------------------------------------------------
# Exercise 7: Extracting Information
# The variable 'data' is a student record in the format "name:age"
# Use string slicing and string methods to extract the name and the age
# and print the result formatted.
#
# data = "lucy smith:28"
#
# Expected output:
# Name: Lucy Smith
# Age: 28

data = "lucy smith:28"
s_data = str(data)
first_name = (s_data[0:4]).title()
last_name = (s_data[5:10]).title()
age = s_data[-2:]
print(f'Name: {first_name} {last_name} \n Age: {age}')

# ---------------------------------------------------------------------
# Exercise 8: Miles to Kilometers Conversion
# Write a program that converts a distance in miles to kilometers.
# Take the distance in miles as input, convert it to kilometers
# using the formula miles * 1.6, and display the
# result using f-strings.

# Example Input: 10
# Example Output: 10 miles is approximately 16.0 kilometers.

# We are converting the input string to float:
# Input: float("1.23")
# Output: 1.23
miles = float(input("Enter distance in miles: "))
kilometers = miles * 1.6

print(f'{int(miles)} miles is approximately {kilometers} kilometers')


# ---------------------------------------------------------------------
# Exercise 9: Workouts calculator
# Write a Python program that asks the user to input the number
# of minutes spent on three different exercises: cardio, strength
# training, and yoga using the input() function. Convert the input
# strings to integers using the int() function. Calculate the
# total time spent on workouts by summing up the minutes from all
# three activities. Based on the total workout time, provide a
# motivational message using an f-string that encourages the user
# to stay consistent and reach their fitness goals. Display the
# motivational message to the user.

cardio = int(input('Enter your minutes of cardio: '))
strength_training = int(input('Enter your minutes of strength training: '))
yoga = int(input('Enter your minutes of yoga: '))
total_time = str(cardio + strength_training + yoga)
print(f'Great job! You have worked out for {total_time} minutes!\n '
         f'Next time it\'s going to be even more time in the gym!' )

# ---------------------------------------------------------------------
# Challenge 1 (OPTIONAL!): Reverse the negative integer -324 and keep
# the negative symbol. Expected output: -423
input_number = -324

# Convert the integer to a string to handle the negative symbol separately
num_str = str(input_number)

# Reverse the digits (excluding the negative symbol) using slicing [::-1]
# Use this simple guide to help you slice the reversed string:
# http://bit.ly/3siP47n

# (ADD YOUR CODE BELOW)
reversed_str = num_str[3:0:-1]
# Add the negative symbol back to the reversed string
reversed_num = int(num_str[0] + reversed_str)

# Output the result
# (ADD YOUR CODE BELOW)
print(reversed_num)
# ---------------------------------------------------------------------
# Challenge 2 (OPTIONAL!): Formatting Average Speed
# In this exercise, we're developing a program to determine the
# average speed of a truck based on the distance traveled in miles
# and the total time taken in hours. Your task is to format and display
# this average speed accurately.
# Task:
# Your program should take the number of miles and the total number
# of hours traveled as input and calculate the average speed. Then,
# present the average speed in a user-friendly format, rounded to one
# decimal place.
#
# Example:
# If the driver covered 60 miles in 3 hours, the calculated average
# speed is 20.0 miles per hour. However, we want to display it as
# 'The average speed is 20.0 miles per hour'.
#
# Similarly, for 55 miles and 3 hours, the calculated speed is
#  approximately 18.33333333332, but we want to format and display
#  it as 'The average speed is 18.3 miles per hour'.
#
# Hints:
# Refer to the "Format examples" section in the official Python
# documentation for string formatting techniques:
# https://docs.python.org/3/library/string.html#format-examples
# Experiment with different formatting options to achieve the
# desired presentation of the average speed.

# Taking input for miles and hours
miles = int(input("Enter the number of miles: "))
hours = int(input("Enter the total number of hours: "))

# Calculating average speed
average_speed = miles / hours

# Formatting and displaying the result
# (Your code here)
rounded_speed = round(average_speed,1)
print(f"The average speed is {rounded_speed} miles per hour")
