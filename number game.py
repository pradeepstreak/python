import random
hidden = random.randrange(1,201)
print(hidden)
guess = int(input("Enter your guess:"))
if guess == hidden:
    print("Hit!!!!")
elif guess < hidden:
    print("miss!!!!")
    
