import random
from string import capwords

print("Lets Play Rock Paper Scissors")

def Main():
    
    Choices = ["Rock", "Paper", "Scissors"]
  
    print("""Rules: 
    \nYou should only Pick"""+ "\n")
    for c in Choices:
        print(c)
    
    
    People = input("\nEnter your Choice here: ")
    Computer = random.choice(Choices)
    People = capwords(People)

    
    print("\nYour Pick is: " + People)
    print("Computer pick is: " + Computer + "\n")

    if People == Computer:
        print("The pick is draw")
    elif People == "Rock":
        if Computer == "Scissors":
            print("You Win!")
        else:
            print("You Lose!")
    elif People == "Paper":
        if Computer == "Rock":
            print("You Win!")
        else:
            print("You Lose!" )
    elif People == "Paper":
        if Computer == "Scissors":
            print("You Lose")
        else:
            print("You Win")
    elif People == "Scissors":
        if Computer == "Rock":
            print("You Lose")
        else:
            print("You Win")
    else: 
        print("Invalid Option")

    Exit()

def Exit():
    
    
    
    User = input("\nYou want to Continue Press 0 and 1 to Exit: ")
    
    if User == "0":
        Main()
    elif User == "1":
        print("\nThank you for playing the Bato Bato Pick")
        quit()
        
        
        
    

    
        
        
    
    
if __name__ == "__main__":
    Main()
    Exit()
    