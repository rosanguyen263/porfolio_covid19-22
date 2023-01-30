from random import randint
from time import sleep

enlight = "######### "

def get_choice():
    x = input("Write here the number then hit <Enter>:")
    return x

def menu():
    print("Choose the number of your choice")
    print("1 - stone")
    print("2 - paper")
    print("3 - scissors")
    print("4 - exit")
    app(get_choice())
    
def app(user_input):
    try:
        user_input = int(user_input)
    except:
        pass
    computer = randint(1,3)
    possibilities = [1,2,3,4]
    if user_input not in possibilities:
        print("You need to choose from 1 or 2 or 3 from the menu. ")
        menu()

    if user_input == computer:
        print(enlight + "draw")
        sleep(3)
        menu()

    if user_input == 1 and computer == 2:
        print(enlight + "Computer won. Your choice: stone. Computer choice: paper")
        sleep(3) 
        menu()
        
    if user_input == 1 and computer == 3:
        print(enlight + "You won. Your choice: stone. Computer choice: scissors")
        sleep(3)
        menu()
         
    if user_input == 2 and computer == 3:
        print(enlight + "Computer won. Your choice: paper. Computer choice: scissors") 
        sleep(3)      
        menu()
        
    if user_input == 2 and computer == 1:
        print(enlight + "You won. Your choice: paper. Computer choice: stone") 
        sleep(3)      
        menu()    
        
    if user_input == 3 and computer == 2:
        print(enlight + "You won. Your choice: scissors. Computer choice: paper") 
        sleep(3)      
        menu()
        
    if user_input == 3 and computer == 1:
        print(enlight + "Computer won. Your choice: scissors. Computer choice: stone")  
        sleep(3)     
        menu()   
        
    if user_input == 4:
        pass

        
        
menu()   
