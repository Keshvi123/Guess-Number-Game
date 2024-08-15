import random

num=random.randint(1,1000)
guess=-1
list=[]
while(guess!=num):
    guess=int(input("Guess number from 1 to 1000 "))
    list.append(guess)
    if(guess>num):
        print("Your Guess is so High , Lower number Please!!")
    elif(guess<num):
        print("Your Guess is so Low , Higher number Please!!") 
    else:
        print("Your Guess is Correct!! It was ",guess)   

print("List of Your Guesses is : ",list)   
