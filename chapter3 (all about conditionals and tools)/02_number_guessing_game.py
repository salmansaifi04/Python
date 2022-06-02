# winning_number = 25
# guss_number = int(input("Enter the number b/w 1 to 100 : "))
# if winning_number == guss_number:
#     print("You win!!!")
# else:
#     if guss_number > winning_number:
#         print("too high")
#     else:
#         print("too low")


import random
winning_number = random.randint(1,100)
user_input = int(input("Guess a number between 1 to 100 : "))
guess_time = 1
while True:
    if winning_number == user_input:
        print(f"You win!!!, you guess in {guess_time} time")
        break
    else:
        if winning_number>user_input:
            print("Too Low")
        else:
            print("Too High")    
        guess_time+=1
        user_input = int(input("guess again :"))