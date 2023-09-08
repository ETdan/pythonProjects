from random import randint
import data
import art
import os

score=0
right=True
print(art.logo)

first=data.data[randint(0,len(data.data)-1)]
while right==True:
    second=data.data[randint(0,len(data.data)-1)]

    print(f"compare A: {first['name']}, {first ['description']} , {first ['country']}")
    print(art.vs)
    print(f"compare B: {second ['name']}, {second ['description']} , {second ['country']}")

    choice=input("who has more followers? type 'A' or 'B': ")
    os.system('cls')
    if choice.lower()=='a' and first['follower_count'] > second['follower_count']:
        score+=1
        print(art.logo)
        first=second
        print(f"you are right! Current score: {score}")
    elif choice.lower()=='b' and first['follower_count'] < second['follower_count']:
        score+=1
        print(art.logo)
        first=second
        print(f"you are right! Current score: {score}")
    else:
        print(art.logo)
        print(f"you got it wrong Current score: {score}")
        Continue=input('Do u want to contiue? type "y" or "n": ')
        if Continue.lower()=='y':
            score=0
            first=data.data[randint(0,len(data.data)-1)]
        else:
            right=False