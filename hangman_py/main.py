import random,hangman,words

print(hangman.logo)
play = input("press y/n: ")

while(play == 'y' or play== "Y"):
    word=words.words[random.randint(0,len(words.words)-1)]
    gusserword=""
    for a in word:
        gusserword+="_"
    updated_gusserword=""
    i=0
    while gusserword!=word and i!=len(hangman.hangman):
        print(gusserword)
        print(hangman.hangman[i])
        letter=input("gusee a letter: ")
        if letter in words.gussedrwords:
          print(f"\nyou have alrady gussed {letter}\n")
        else:
          words.gussedrwords.append(letter)
          if letter in word:
              for a in range(len(word)):
                  if word[a] == letter:
                     updated_gusserword+=letter
                  else:
                     updated_gusserword+=gusserword[a]
              gusserword=updated_gusserword
              updated_gusserword=""        
          else:
              i+=1
    if(gusserword==word):
        print(hangman.win_logo)
    else:
        print(hangman.loose_dead_logo)
        print(hangman.loose_logo)
        print(f"\nThe word was {word}\n")
    words.gussedrwords.clear()
    play = input("press y/n: ")
