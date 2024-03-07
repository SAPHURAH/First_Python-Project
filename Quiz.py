print("welcome to my python quiz!")

playing= input("Do you want to play my game? ")

if playing !=  "Yes":
    quit()

print("Okay ! let's play ):")

Score = 0

answer = input( " Is python a programming language? ").upper()

if answer == "Yes":
    print("Well Done !")
    Score +=1
else:print("Try again!")

answer = input( " What created python? ").lower()

if answer == "Guido van Rossum":
    print("Correctomundo!")
    Score +=1
else:print("Incorrect!")

answer = input( " Which year was python released? ")

if answer == "1991":
    print("That's Good!")
    Score +=1
else:print("Come Again!")

answer = input( " What can python be used for? ")

if answer .lower()== "Web Development, Software Development , Mathematics":

    print("Wow! That's interesting")
    Score +=1
else:print("Try one more time!")

answer = input( " Many PCs and Macs will have python already installed. ").lower()

if answer == "True":
    print("Bravo !")
    Score +=1
else:print("Try again!")

answer = input( " Python syntax can be executed by writing directly in the Command Line. ")

if answer .upper()== "True":
    print("Well Done !")
    Score +=1
else:print("Try again!")

answer = input( " The indentation in Python is very important. ")

if answer == "True":
    print("Great Job !")
    Score +=1
else:print("Try again!")

answer = input( " In Python, variables are created when you assign a value to it? ")

if answer == "True":
    print("Nice one there!")
    Score +=1
else:print("Incorrect!")

answer = input( " Comments can be used to explain Python code. ")

if answer == "True":
    print("Well Done !")
    Score +=1
else:print("You can do better!")

answer = input( " Variables are containers for storing data values  ")

if answer .upper()== "True":
    print("Well Done !")
    Score +=1
else:print("Try again!")

answer = input( " String variables can be declared either by using single or double quotes? ")

if answer.lower() == "Yes":
    print("Excellent!")
    Score +=1
else:print("Oops!")


print("You got  " + (str(Score/10)*100 )+ "%")