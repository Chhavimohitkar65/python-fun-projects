from ast import If
import pyttsx3
engine = pyttsx3.init()
engine.say("GOOD MORNING . \n DEAR USER PLEASE ENTER YOUR GOOD NAME")
engine.runAndWait()
name = input ("PLEASE ENTER YOUR GOOD NAME: ")
engine.say("Dear")
engine.say(name)
engine.say("Please enter two numbers")
engine.runAndWait()
number_1 = int(input('Pleasse enter 1st number:-  '))
number_2 = int(input('Pleasse enter 2nd number:-  '))
print("num1 = ",number_1,"\nnum2 = ", number_2)
engine.say(number_1)
engine.say(number_2)
engine.say("Are the two numbers. What would you like to do with the following numbers")
engine.runAndWait()
operation = input("+ , - , % , *\n")
if operation == "+":
    engine.say("Sum of two numbers is")   
    sum = number_1 + number_2
    engine.say(sum)
    engine.runAndWait()  
    print("Sum of two numbers is ",sum ) 
elif operation == "-":
      engine.say("substraction of two numbers is")
      substraction = number_1 - number_2
      engine.say(substraction)
      engine.runAndWait()
      print(" substraction of two numbers is ",substraction ) 
elif operation =="*":
    engine.say("multiplication of two numbers " )
    multiplication = number_1 * number_2
    engine.say(multiplication)
    engine.runAndWait()
    print(" multiplication of two numbers is ",multiplication)    
else:
    engine.say("division of the two number is" )  
    division = number_1 % number_2
    engine.say(division) 
    engine.runAndWait()
    print(" division of two numbers is ", division) 
engine.say(name)
engine.say("Thank you for using me")
engine.runAndWait()    
        
     





    


    
