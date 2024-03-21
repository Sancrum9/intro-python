# Midterm quiz. 
# Create a new python document called midtermquiz.py
# Complete the following questions.
# Once you have comepleted your quiz, commit and sync your work to your GitHub. 

#RULES
# This quiz is open book; you may use your notes, google (only if you are viewing arcticles about python), W3schools only. Any other website
# is prohibitied.
# No phones are allowed during the quiz. refusal to put away a phone will result in failure.
# There is no talking during the quiz. If you complete the quiz, notify the instructor that you
# have finished. Once that is done, you are free to use your device and browse the web quitely. 

# Good Luck

# 1. In your own words, describe what the difference
# between a function arguement and a function parameter.
# Write your response using complete sentences.
#The values that are defind within a function when the function is called are called argument.
#The variables that are defined when the function is defind are called parameters.
# 2. In your own words, describe what each of the following errors means.
# Write your response using complete sentences.

# syntax error: Not speaking the computers language
# type error: A TypeError is raised when an operation or function is applied to an object of an inappropriate type. 
# name error: A NameError is raised when the program attempts to access or use a variable that has not been defined or assigned a value. 

# 3. What function would I use if I wanted to convert an integer data type into 
# a string data type?
#I would use str() function
# 4. What function would I use if I wanted to change a float data type into a 
# an integer data type?
#I would use the int() function
# 5. Describe three (3) Variable naming rules. Write your response in complete sentences. 
#Camel Case, Pascal Case, Snake Case
# 6. Name the operator family each of these symbols are a part of 
# and describe how each of these sybmols are used. Write your response
# useing complete sentences. 

#symbols
# = 
# == 
# =!
# These operator symbols are apart of the arithatic operators
# 7. You have been hired as an engineer to develop a car speed detection system.
# the car company would like to create a function where if the user goes over a certain
# speed it will notify them to change gears. The client has provided you with the following
# guidelines on how they would like the gear system to work:
# if the driver is going over 20mph, alert the driver to shift to gear 1
# if the the driver is going over 30mph, alert the driver to shift to gear 2
# if the driver is going over 40mph, alert the driver to shift to gear 3
# if the driver is going over 70mph, alert the driver to shift back to gear 1.
# the client would like you to pass in the speed that the user is going as an argument. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.
mph= "miles per hour"
def GearShift(speedlimit):
    speedlimit == mph
    if speedlimit == "20mph":
        print(f"Activate gear 1")
    elif speedlimit == "21mph":
        print(f"Activate gear 1")
    elif speedlimit ==  "22mph":
        print(f"Activate gear 1")
    elif speedlimit == "23mph":
        print(f"Activate gear 1")
    elif speedlimit == "24mph":
        print(f"Activate gear 1")
    elif speedlimit == "25mph":
        print(f"Activate gear 1")
    elif speedlimit == "26mph":
        print(f"Activate gear 1")
    elif speedlimit == "27mph":
        print(f"Activate gear 1")
    elif speedlimit == "28mph":
        print(f"Activate gear 1")
    elif speedlimit == "29mph":
        print(f"Activate gear 1")
    elif speedlimit == "30mph":
        print(f"Activate gear 1")
    elif speedlimit == "31mph":
        print(f"Activate gear 2")
    elif speedlimit == "32mph":
        print(f"Activate gear 2")
    elif speedlimit == "33mph":
        print(f"Activate gear 2")
    elif speedlimit == "34pmh":
        print(f"Activate gear 2")
    elif speedlimit == "35mph":
        print(f"Activate gear 2")
    elif speedlimit == "36mph":
        print(f"Activate gear 2")
    elif speedlimit == "37mph":
        print(f"Activate gear 2")
    elif speedlimit == "38mph":
        print(f"Activate gear 2")
    elif speedlimit == "39mph":
        print(f"Activate gear 2")
    elif speedlimit == "40mph":
        print(f"Activate gear 2")
    elif speedlimit == "41mph":
        print(f"Activate gear 3")
    elif speedlimit == "42mph":
        print(f"Activate gear 3")
    elif speedlimit == "43mph":
        print(f"Activate gear 3")
    elif speedlimit == "44mph":
        print(f"Activate gear 3")
    elif speedlimit == "45mph":
        print(f"Activate gear 3")
    elif speedlimit == "46mph":
        print(f"Activate gear 3")
    elif speedlimit == "47mph":
        print(f"Activate gear 3")
    elif speedlimit == "48mph":
        print(f"Activate gear 3")
    elif speedlimit == "49mph":
        print(f"Activate gear 3")
    elif speedlimit == "50mph":
        print(f"Activate gear 3")
    elif speedlimit == "51mph":
        print(f"Activate gear 3")
    elif speedlimit == "52mph":
        print(f"Activate gear 3")
    elif speedlimit == "53mph":
        print(f"Activate gear 3")
    elif speedlimit == "54mph":
        print(f"Activate gear 3")
    elif speedlimit == "55mph":
        print(f"Activate gear 3")
    elif speedlimit == "56mph":
        print(f"Activate gear 3")
    elif speedlimit == "57mph":
        print(f"Activate gear 3")
    elif speedlimit == "58mph":
        print(f"Activate gear 3")
    elif speedlimit == "59mph":
        print(f"Activate gear 3")
    elif speedlimit == "60mph":
        print(f"Activate gear 3")
    elif speedlimit == "61mph":
        print(f"Activate gear 3")
    elif speedlimit == "62mph":
        print(f"Activate gear 3")
    elif speedlimit == "63mph":
        print(f"Activate gear 3")
    elif speedlimit == "64mph":
        print(f"Activate gear 3")
    elif speedlimit == "65mph":
        print(f"Activate gear 3")
    elif speedlimit == "66mph":
        print(f"Activate gear 3")
    elif speedlimit == "67mph":
        print(f"Activate gear 3")
    elif speedlimit == "68mph":
        print(f"Activate gear 3")
    elif speedlimit == "69mph":
        print(f"Activate gear 3")
    elif speedlimit == "70mph":
        print(f"Activate gear 3")
    else:
        speedlimit == "71mph"
        print(f"Activate gear 1")
GearShift("70mph")
    

# 8. You have been hired as an engineer to develop a fitness meal plan program. 
# your function should take in two (2) arguements; the day of the week, and the time of the day.
# depending on the time of the day; either morning or afternoon, the meal plan will change. 
# the client has provided you with the following meal plan information
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

monday_morning= "2 eggs and an apple"
monday_afternoon= "bbq grilled chicken and broccoli"

tuesdaymorning= "oatmeal with strawberries and blueberries"
tuesdayafternoon= "baked chicken with kale"

wednesdaymorning= "fruit salad"
wednesdayafternoon= "curry goat with rice and cabbage"

thursdaymorning= "pancakes and turkey sausage"
thursdayafternoon= "eggplant pasta"

fridaymorning= "steak and eggs"
fridayafternoon= "cheesburger and fries"

saturdaymorning= "oatmeal"
saturdaynight= "baked chicken with string beans"

sundaymorning = "oatmeal"
sundaynight = "steak and spinach"
def mealProgram(program):
    if program== monday_morning:
        print(monday_morning)
    elif program == monday_afternoon:
        print(monday_afternoon)
    elif program == tuesdaymorning:
        print(tuesdaymorning)
    elif program == tuesdayafternoon:
        print(tuesdayafternoon)
    elif program == wednesdaymorning:
        print(wednesdaymorning)
    elif program == wednesdayafternoon:
        print(wednesdayafternoon)
    elif program == thursdaymorning:
        print(thursdaymorning)
    elif program == thursdayafternoon:
        print(thursdayafternoon)
    elif program == fridaymorning:
        print(fridaymorning)
    elif program == fridayafternoon:
        print(fridayafternoon)
    elif program == saturdaymorning:
        print(saturdaymorning)
    elif program == saturdaynight:
        print(saturdaynight)
    elif program == sundaymorning:
        print(sundaymorning)
    elif program == saturdaynight:
        print(saturdaynight)
    else:
        print(f"Error: I dont understand what you are saying")
mealProgram(fridayafternoon)
    

# 9. You have been hired as an enineer to develop a school to develop an academic honors system.
# the client would like to check if the user has gotten above an 85% overall grade or has
# has accomplished passing the SAT. The client would like you to pass this information in as
# arguements. If either of these situations are true the student has made the academic honors list
# if only passing the SAT is true, congratulate the user but inform them they did not make the list.
# if they only scored above 85%, congratulate the user but inform them they did not make the list.
# if none of the conditions are met, inform them to continue studying and try again next semester. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# 10. Create a function that will check the temperature outside. If the user enters
# a number above 60 degrees it is warm outside, if the enter a number above 80 degrees it is hot outside.
# if the user enters a number below 50 degrees it is cold outside. and if the tempeature is above 50 degrees,
# tell the user it's not warm but it's also not too cold. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.