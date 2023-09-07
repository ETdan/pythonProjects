import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def getCards(numberOfCard):
    '''
    :param1 Number of cards
    
    :return List of Cards and Sum of Cards
    '''
    List=[]
    sum=0
    while numberOfCard:
        val=cards[random.randint(0,len(cards)-1)]
        sum+=val
        List.append(val)
        numberOfCard-=1
    return List, sum
logo="""

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/    

"""