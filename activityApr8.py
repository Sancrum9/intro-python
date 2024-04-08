# Async Activity April 8th, 2024

# 1. In your own words, describe what a while loop is?
#The way i would describe a while loop is, As long as functiion is true put this place that

#2. Create a function that uses a while loop to determine if a user has typed in 
# the the correct word guess. If the user types in the wrong word, your program 
# should inform them that their guess was inccorect and to try again, but if the
# user guesses the word correctly, your program shoul tell the user they have 
# guessed correctly and have won the game, stopping the loop.

UserInput = input('Please enter your passcode.  ')

while UserInput != '12345':
    print('Password is incorrect')
    print('Wait five more seconds. ')
    print('4')
    print('3')
    print('2')
    print('1')
    UserInput = input('Please enter your password.  ')
if UserInput == '12345':
    print('Correct password, welcome.  ')