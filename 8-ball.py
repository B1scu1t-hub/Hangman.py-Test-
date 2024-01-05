import random
from re import U

name = input('How can I help you? Put your name in to Begin')
# User is asked to to input name.

print("Ight bro ur gonna get wrecked. Best of luck" + " " + name + "!")

#nums = [1, 2, 3, 4, 5, 6, 7, 8]



#nums = random.choice(nums)
#print('Enter number')
userNum = int(input('Put a number in my dude'))

turns = 22

while turns > 0:


    if userNum == 1:
        print("He was number ONE!!!!!!")
        turns -= 1
        break
            

    elif userNum == 2:
        print("Bro 2 is for fools my boi")
        break
            

    elif userNum == 3:
        print("3 is for frees")
        break
            

    elif userNum == 4:
        print("Oh god we're starting to get a little deep here.")
        break
            

    elif userNum == 5:

        print('Give me a high ___')
        break
            

    elif userNum == 6:
        print('6 to get ur fix my dude')
        break
            

    elif userNum == 7:
        print('Lucky number seven baby!')
        break
            

    elif userNum == 8:
        print('The final one!')
        break
            

    elif userNum > 8:
        print('Invalid Number, Exiting Game')
        break

    
        
