import random

level={"hard":5,"easy":10}

print("I'm  thinking of a number between 1 and 100.")
choosed_level=input("choose  difficulty type 'hard' or 'easy' for the level: ")

choosed_level=level[choosed_level]
number=random.randint(1,100)

while choosed_level:
    print(f"you have {choosed_level} attempts remainig to guess a number .")
    gusses=int(input("make a guess: "))
    if gusses > number:
        print('too high')
    elif gusses < number:
        print('too low')
    elif gusses ==number:
        print('YOU GOT IT!!!')
        break
    choosed_level-=1
if choosed_level == 0:
    print(f"the number was {number} better luck next time")