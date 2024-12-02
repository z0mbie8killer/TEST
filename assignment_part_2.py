"""
Author: Cezar Hernandez
Date created: 11/24/2024
Assignment: Module 5 Programming Assignment part 2
Description: this script is a random number guessing game. The user inputs a number to see if it's
the random number the computer generated in the script. It checks to make sure you put in a vaild
input, and if your guess has to be higher or lower.
"""
import random
user_vaildation = True
random_number = random.randint(1,100)

num_list = []
def chk_input_isnumber(inn): #checks to make sure the input is just a number only
    num_let_chk = 0
    if  any(num_let_chk.isdigit() for num_let_chk in inn ) and any( num_let_chk.isalpha() for
    num_let_chk in inn ) == True: # this is checking if the string contains a letter and a #
        return False
    elif inn.isalpha() == True:  # this is checking if the string contains a letter
        return False
    else:
        return True
#print(random_number) #this is to show what your random number is that's why it's commented out
while user_vaildation == True: #starts while loop
    user_input = input("enter your guess(must be 0-100) press enter to exit") #the user input
    if user_input == "":#checks if the your pressed enter, if so quit program
        user_vaildation = False
    elif chk_input_isnumber(user_input) == False:#checks to make sure the input is just a number
        print("invaild input")
    else:
        user_input = int(user_input) #changes the user_input to a intager 
        if user_input > random_number:#the number you input is greater then the random number
            print("the number is lower")
        elif user_input < random_number:#the number you input is greater then the random number
            print("the number is higher")
        elif user_input == random_number:#the number you input is less then the random number
            print("you've found the right number ", user_input," the number has been changed")
            num_list.append(random_number)#adds to a list, that shows all the random numbers found
            random_number = random.randint(1,100) #create a new random number
            #print(random_number) #this is to show what your random number is that's why it's commented out

print( "the numbers you found: " , num_list)#show all the random numbers you found
