# Async Assignment March 3rd, 2024. 

# Complete and solve the following prompts.
# Make sure to write down the clues and keywords you found.
# (Make sure to include your clues and keywords to recieve full credit)

# Commit and sync your work before the end of class. 
# This will count toward your class activity grade. 

# Prompt #1- Elevator Conditional Function Execercise.

# You have been hired by a architeture firm to assist 
# with developing their elevator system. They have asked 
# you to develop a function that will accept a user's input. 
# your program should ask the user to enter a floor number. 
# When an user enters a number they will be sent to a specific 
# floor in the building. If the user enters a floor number that does not
# exist, your program should inform the user that the floor they entered
# does not exist and to enter another number and to try agin.

# The architects have given you the following 
# lists of floors for their building:

Lobby = 'L'
Basement = 'B'
Rooftop = 'R'
Gym = '1'
Restuarant = '2'
Work_space = '3'
Living_quarter= '4'

def ElevatorSystem():
    floors = input('what floor would u like to go too ')
    if floors ==Lobby:
        print('you are going to the lobby')

    elif floors ==Basement:
        print("your going to the basement")
    elif floors ==Rooftop:
        print("your going to the rooftop")
    elif floors ==Gym:
        print("your going to the 1st floor")
    elif floors ==Restuarant:
        print("your going to the 2nd floor")
    elif floors ==Work_space:
        print("your going to the 3rd floor")
    elif floors ==Living_quarter:
        print("your going to the 4th floor")
    else:
        print('your floor does not exist')
ElevatorSystem()

#___________________________________________________________

# Prompt #2- Amusement Park Conditional Function
# You have been hired by an amusement park to develop a function
# that allows users to access their roller coasters by entering their age
# and height. Your program should take the user's height and age as parameters.
# Your client has very specific requirements for thier guests 
# to ride their roller coasters and have provided you with the following 
# conditions that they would like your program to check for. 

# user must be atleast 5.2 or taller and atleast 14 years old or older 
# in order to ride roller coaster 1. 

# if the user is shorter than 5.2 but at least 14 years of age or older,
# they can ride the roller coaster 2.

# if the user is shorter than 5.2 and also younger than 14 years of age,
# they can ride roller coaster 3. 

# if the user enters information incorrectly, give them an error message
# and tell them that they entered their information incorrectly. 
#def check_roller_coaster_eligibility(age,height):
 #   if age>= 14 and height>= 5.2:
 #       print("You can get on roller coaster #1. ")
 #   elif age>= 14 and height< 5.2:
 #       print("you can get on roller coaster #2. ")
  #  elif age< 14 and height< 5.2:
 #       print("you can get on roller coaster #3. ")
 #   else:
 #       print("error; please try again. the information you have provided is not availabe for these coasters")

#check_roller_coaster_eligibility(5.9,10)