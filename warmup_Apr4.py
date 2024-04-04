#The way i would describe a while loop is, As long as functiion is true put this place that
# 
def checkBday():
    month=[0,1,2,3,4,5,6,7,8,9,10,11,12]
    day=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    bday=[month[1],day[1]]
    print(f"birthdate is {bday}")
    userInput=[]

    while userInput != bday:
        userInput_Month = int(input(f"please enter the correct month: "))
        userInput_Day = int(input(f"please eneter the correct day: "))
        userInput.append(userInput_Month)
        userInput.append(userInput_Day)
        userInput.clear()
        print(f"number stored in userInput: {userInput}")
        if userInput == bday:
            print(f"congrats! HappyBday")
checkBday()