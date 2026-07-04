print("Welcome to Number Guessing Game!")
print("********************************
      ")
import random
num=random.randint(1,100)
Attempt=0
while True:
    guess=int(input("Guess the Number between 1 t0 100:"))
    Attempt+=1
    if guess==num:
        print("Congratulations! yoou guessed the number in "+str(Attempt)+"attempts.")
        break
    elif guess<num:
        print("Too Low")
    elif guess>num:
        print("Too High")
       
