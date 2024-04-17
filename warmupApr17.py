# Warm up Tuesday April 16th, 2024.

import random

# 1. In your own words, explain the difference between an Python For Loop and a
# Python While Loop.
#while loops keep running as long as the conditioun is true
#For loop ia a function used to iterate over a sequence

# 2. Create a loop that will iterate over a list of numbers. For evey number in your loop,
# it should multiply that number by 3. 

#numberList=[1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99,111,222,333,444,555,666,777,888,999]

#for number in numberList:
#    print(number * 3)

# 3. Use the following code snippet below to create a guessing game function. 
# The code below will generate a random number for you. You must write a loop that will
# ask the user to input their guess, if they guess incorrectly, the program will repeat 
# itself and ask the user to guess again. The program should continue to ask them to
# guess until they've gotten it correctly. Once they guess the correct number the program
# will congratulate them and the loop will stop. 

# generates a random number between 1 and 10
randomNumber = random.randint(1, 10)
print(f'Random number value is: {randomNumber}')
userInput= int(input("enter your guess:"))
while userInput != randomNumber:
    print("Incorrect. Try again:")
    userInput= int(input("Re-enter your Guess:"))
    if userInput== randomNumber:
        print("Congrats! youve guessed correct")
        print("Ending loop")