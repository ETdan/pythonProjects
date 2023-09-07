import cards,os

play= input("do you want to play BlackJack 'y'/'n': ")
os.system('cls')

while play=='y':
    print(f"{cards.logo}")
    List=[]
    userList=[]
    compList=[]
    userSum=0
    compSum=0
    List, userSum = cards.getCards(2)

    userList.extend(List)

    List,compSum = cards.getCards(2)
    compList.extend(List)

    print(f"Your cards: {userList}, current score: {userSum}")

    print(f"computers first card: {compList[0]}")

    if userSum==21:
        if compSum==21:
            print("tie")
        else:
            print("you win!!")
    else:
        Continue=input("Type 'y' to get another card, type 'n' to pass: ")
        os.system('cls')

        if Continue=='y':
            while Continue =='y' and userSum < 21:
                List,sum=cards.getCards(1)
                if List[0]==11:
                    if List[0] + userSum >21:
                        userList.append(1)
                        userSum+=1
                else:
                    userList.extend(List)
                    userSum+=sum

                if userSum ==21:
                    os.system("cls")
                    print(f"Your cards: {userList}, current score: {userSum}")
                    print("you win!!\n")
                    break
                elif userSum >21:
                    os.system("cls")
                    print(f"Your cards: {userList}, current score: {userSum}")
                    print("You went over. You lose!!\n")
                    break
                else:
                    print(f"Your cards: {userList}, current score: {userSum}")
                    print(f"computers first card: {compList[0]}")

                Continue=input("Type 'y' to get another card, type 'n' to pass: ")

        if Continue == 'n':
            while compSum < 21 and compSum < userSum:
                List,sum=cards.getCards(1)
                if List[0]==11:
                    if List[0] + compSum >21:
                        compList.append(1)
                        compSum+=1
                else:
                    compList.extend(List)
                    compSum+=sum

            if compSum >21:
                print(f"final hand: {userList}, final score: {userSum}")
                print(f"final computers cards: {compList}, final score:{compSum}")
                print("you win!!\n")
            elif compSum == userSum:
                print(f"final hand: {userList}, final score: {userSum}")
                print(f"final computers cards: {compList}, final score:{compSum}")
                print("tie!\n")
            else :
                print(f"final hand: {userList}, final score: {userSum}")
                print(f"final computers cards: {compList}, final score:{compSum}")
                print("you lose!!\n")
    play= input("do you want to play BlackJack 'y'/'n': ")
    os.system('cls')

# print(userSum, userList)
# print(compSum, compList)