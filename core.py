import random
import time

def count_total(cards):
    total = 0
    for card in cards:
        total += card
    return total

def firstmix(cards,ucards,bcards):
    randomcard = random.randint(0,10)
    ucards.append(cards[randomcard]) 
    cards.pop(randomcard)

    randomcard = random.randint(0,9)
    bcards.append(cards[randomcard])
    cards.pop(randomcard)

def user_turn(cards,ucards,mbcards):
    utotal = count_total(ucards)
    mbtotal = count_total(mbcards)

    print("Player turn!")
    print("Your cards:",ucards,"|",utotal,"/",21)
    print("Bot cards:",mbcards,"|",mbtotal,"+ ?","/",21)
    print("1 - Take one card; 2 - Pass;")
    choice = int(input(">> "))
    
    if (choice == 1):
        if (utotal<21):
            randomcard = random.randint(0,len(cards)-1)
            ucards.append(cards[randomcard])
            print("You took:",end="")
            time.sleep(1)
            print(cards[randomcard])
            cards.pop(randomcard)
            print("--------------------")
            time.sleep(3)
            return 1
        elif (utotal == 21):
            print("Enough for you!")
            return 2
        elif (utotal > 21):
            print("Too much for you...")
            return 2
    if (choice == 2):
        print("You're passing.")
        return 2
        
def bot_turn(cards,bcards,mucards):
    avaiblecards = [1,2,3,4,5,6,7,8,9,10,11]
    btotal = count_total(bcards)
    mutotal = count_total(mucards)

    if (btotal >= 21 or mutotal >= 21):
        print("Bot passing.")
        return 2
    else:
        for card in bcards:
            avaiblecards.remove(card)
        for card in mucards:
            avaiblecards.remove(card)

        ndcard = 21-btotal
        ndcardtotal = 0

        for card in avaiblecards:
            if (card<=ndcard):
                ndcardtotal+=1
        
        chances = ndcardtotal/len(avaiblecards)
        
        if (chances>=1):
            randomcard = random.randint(0,len(cards)-1)
            bcards.append(cards[randomcard])
            print("Bot taking card.")
            print("The card is:", end="")
            time.sleep(1)
            print(cards[randomcard])
            cards.pop(randomcard)                                                            
            print("--------------------")
            return 1
        else:
            print("Bot passing.")
            return 2

def check_pass(upass,bpass):
    if (upass == 2 and bpass == 2):
        return 1
    else:
        return 0

def match_results(ucards,bcards):
    utotal = count_total(ucards)
    btotal = count_total(bcards)

    if (utotal <= 21 and btotal > 21):
        return 1
    if (utotal > 21 and btotal <= 21):
        return 2
    if (utotal <= 21 and btotal <= 21):
        if (utotal > btotal):
            return 1
        if (btotal > utotal):
            return 2
    if (utotal == btotal):
        return 0
    if (utotal > 21 and btotal > 21):
        if (utotal < btotal):
            return 1
        if (btotal < utotal):
            return 2

def showdown(upoints,bpoints):
    print("User points:",upoints)
    print("Bot points:",bpoints)