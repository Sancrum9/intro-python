# Read the following prompt and answer the 3 questions

# Prompt

# You have been tasked as an engineer to develop a program that controls the lights in a small home.
# When the users uses the lighting control app that you are developing, they will have the ability to 
# turn lights on and off in the entire house. They can turn lights on and off based on the room in the home 
# individually or all the lights in the home at the same time. 
# there are 3 bedrooms, 1 kitchen, 2 bathrooms, a living room, a dining room, and a basement that all
# have lights and can all be manipulated with by using this app. 

# Questions

# 1. Based on the prompt you just read, what is the main goal(s) of the app that you are creating?
# What is the primary objective of your app? Please write your response using complete a complete sentence.
#Main goal(s):
#A. Making an app that can control the lights in the house
#B. Having features that can control indivual lights
# Turning all the lights off at the same time
# 2. What type of research would you need to do to help you develop this app? And are there 
# any questions that you can think of that could give you more context/ information
# that can help you develop this program that wasn't included ? 
# Please write your response in at least 4 complete sentences. 

# 3. Breakdown step- by- step how you would create this program in Python? Your steps do not have
# to be written in code and it does not have to use python keywords- rather your steps 
# should be explained in a way where an engineer can take the information and understand
# what they need to do.  Please be sure to write your steps in complete sentences. 

#Steps:
# 1. we need buttons and commands for eachrrom in the house to turn the lights on and off
# 2. we need a way to represent each room in the house (List).
# 3. we need a function to turn the lights on and off and tell us the state of the room wrather on or off
 

def lightControl():
    house=["unreachable","bdr1","bdr2","bdr3","kitchen","livingr","dinningr","bathroom1","bathroom2","b"]
    print(house)
    print("welcome to the Light control app")
    print("_______________________")
    userAction=input("what would you like me to do: press 1 for specific room, press 2 for all the rooms:")
    if userAction == 1:
        userRoom= int(input("which room would you like to control?"))
        print("______________________")
        print("Bedroom 1 = press 1")
        print("Bedroom 2 = press 2")
        print("Bedroom 3 = press 3")
        userRoom= int(input("which room would you like to control?"))
        print(house[userRoom])
    elif userAction == 2:
        print("would you like to TURN ON or SHUT OFF all the lights? ")

lightControl()

