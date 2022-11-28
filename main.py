import random


Name = input("What is your name?: ")
print(f"Hi {Name} , Welcome to guess the word")
print("You have 8 chances to guess the name we want. In these 8 chances, you are only allowed to enter words. If you want to guess the full name, you lose if it is wrong.")
NamesComputer = ["ali", "reza", "mohammad", "amir", "sina", "ramin", "armin", "saman", "abbas", "arash", "zahra", "fatemeh", "sara", "atefeh", "asal",
                 "sadaf", "roya", "nazanin"]
Computer = random.choice(NamesComputer)
UserChance = 0
Guess = ''
User = int(input("If you want to guess the full name, enter the number 1 and if you want a letter of the name, enter the number 2:"))

while User == 1 and UserChance < 8:
    UserGuessName = input("Enter the desired name:")
    if UserGuessName == Computer:
        print("You win")
        break
    else:
        print(f"You lose! The correct name was {Computer}")
        break

while User == 2 and UserChance < 8:
    UserGuessletter = input("Enter a letter:")
    for i in Computer:
        if UserGuessletter in Computer:
            print(i, end=" ")
    else:
        print("_")
        UserChance += 1