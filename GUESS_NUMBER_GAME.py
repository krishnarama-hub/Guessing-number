
print("""
  _____ _    _ ______  _____ _____   _______ _    _ ______
 / ____| |  | |  ____|/ ____/ ____| |__   __| |  | |  ____|
| |  __| |  | | |__  | (___| (___      | |  | |__| | |__
| | |_ | |  | |  __|  \___ \\___ \     | |  |  __  |  __|
| |__| | |__| | |____ ____) |___) |    | |  | |  | | |____
 \_____|\____/|______|_____/_____/     |_|  |_|  |_|______|

 _   _ _    _ __  __ ____  ______ _____
| \ | | |  | |  \/  |  _ \|  ____|  __ \\
|  \| | |  | | \  / | |_) | |__  | |__) |
| . ` | |  | | |\/| |  _ <|  __| |  _  /
| |\  | |__| | |  | | |_) | |____| | \ \\
|_| \_|\____/|_|  |_|____/|______|_|  \_\\
""")
import random
print("-"*100)
print("Welcome to the game arena !!!----")
print("-"*100)
print("Guess the correct Number and WIN the fight OR lose as a LOSER")
print("-"*100)
easy_level=10

hard_level=5

def choice():
    print("-"*100)
    print("Enter your choice level of the GAME ----")
    print("-"*100)
    turn=input("Choose the level your 'EASY' OR 'HARD':").upper()
    print("-"*100)
    global choose
    choose=0
    
    if turn=="EASY":
        choose+=easy_level
    else:
        choose+=hard_level
    print("-"*100)
    print(f"You have choosen the level {turn}")
    print(f"YOU HAVE {choose} of life /////-----")
    print("-"*100)

computer=random.randint(1,100)
print("-"*100)



def arena():
    global choose
    choice()
    while True:
        print("-"*100)
        user=int(input("Enter your guess number buddy! between (1-100):"))
        print("-"*100)
        if computer==user:
            print("-"*100)
            print("\n"*1)
            print("Congrates!!You win the GAME---")
            print("-"*100)
            print("\n"*1)
            return
            

        elif computer<user:
            print("-"*100)
            print("\n"*1)
            
            print("Your are close but greater than the GUESS NUMBER!!?")
            choose-=1
            print(f"You have left {choose} turns to win this GAME----")


        elif computer>user:
            print("-"*100)
            print("\n"*1)
            
            print("Your are close but less than the GUESS NUMBER!!?")
            choose-=1
            print(f"You have left {choose} turns to win this GAME----")
            print("-"*100)
            print("\n"*1)
            


        else:
            print("-"*100)
            print("\n"*3)
            
            print("Ivalid input 'BUDDY?'.try once again")
            print("-"*100)
            print("\n"*1)
        
        if choose==0:
            print("-"*100)
            print("\n"*1)
                
            print(f"You lose user!!, the computer guess the number is {computer}")
            print("-"*100)
            print("\n"*1)
            
            return
            
    
arena()
    
            
    
