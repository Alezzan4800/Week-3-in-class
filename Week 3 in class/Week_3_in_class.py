#program to transfrer celius to fahrenheit
#then printing the degrees in fahrenheit


c=float(input("Please enter the tempeture in terms of Celcius: "))
f=float(9/5*c+32)

print(f, "Fahrenheit")

#program asking for an guess to see if you guess number
#telling your how you missed


gue=0
t=0
while gue != 33:
    gue=int(input("Please guess a full number: ")) 
    t=t+1

    if(gue>33):
        print("your guess was to high")

    else:
        print("your guess was to low")
print("you got the correct number")
print("It took you",t,"tries")
