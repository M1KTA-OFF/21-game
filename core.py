import random
import time
import colorama as col

col.init()

def count_total(cards):
    total = 0
    for card in cards:
        total += card
    return total

def reset_colors():
    print(col.Fore.RESET + col.Back.RESET, end="")

def greetings():
    banner = open("banner.txt", "r")
    content = banner.read()
    print(col.Fore.YELLOW + content)
    reset_colors()

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

    print(col.Fore.MAGENTA + "Your turn!")
    print(col.Fore.BLUE + "Your cards:" + col.Fore.WHITE + col.Back.CYAN + str(ucards) + col.Fore.YELLOW + col.Back.RESET + " | " + str(utotal) + "/21")
    reset_colors()
    print(col.Fore.LIGHTBLUE_EX + "Bot cards:" + col.Fore.WHITE + col.Back.CYAN + str(mbcards) + col.Fore.YELLOW + col.Back.RESET + " | " + str(mbtotal) + " + ?/21")
    reset_colors()
    print(col.Fore.GREEN + "1 - Take one card;" + col.Fore.YELLOW + " 2 - Pass;")
    reset_colors()
    
    correctinput = False
    while correctinput == False:
        try:
            print(col.Fore.LIGHTBLUE_EX + "->", end="")
            choice = int(input(""))
            correctinput = True
        
        except:
            print(col.Fore.RED + "You entered something unreadable.")
            reset_colors()
    
    if (choice == 1):
        if (utotal<21):
            randomcard = random.randint(0,len(cards)-1)
            ucards.append(cards[randomcard])
            print(col.Fore.YELLOW + "You took:",end="")
            time.sleep(1)
            if (utotal+cards[randomcard] <= 21):
                print(col.Fore.GREEN,cards[randomcard])
            if (utotal+cards[randomcard] > 21):
                print(col.Fore.RED,cards[randomcard])
            reset_colors()
            cards.pop(randomcard)
            time.sleep(3)
            return 1
        elif (utotal == 21):
            print(col.Fore.GREEN + col.Back.LIGHTWHITE_EX + "You already win!")
            reset_colors()
            return 2
        elif (utotal > 21):
            print(col.Fore.RED + col.Back.LIGHTWHITE_EX + "Sorry but it's enough...")
            reset_colors()
            return 2
    if (choice == 2):
        print(col.Fore.YELLOW + col.Back.LIGHTWHITE_EX + "You're passing.")
        reset_colors()
        return 2
        
def bot_turn(cards,bcards,mucards):
    avaiblecards = list(range(1,12))
    btotal = count_total(bcards)
    mutotal = count_total(mucards)

    print(col.Fore.MAGENTA + "Bot turn!")

    if (btotal >= 21 or mutotal >= 21):
        print(col.Fore.YELLOW + col.Back.LIGHTWHITE_EX + "Bot passing.")
        reset_colors()
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
        if (chances>=0.57):
            randomcard = random.randint(0,len(cards)-1)
            bcards.append(cards[randomcard])
            print(col.Fore.GREEN + "Bot taking card.")
            print(col.Fore.YELLOW + "The card is:", end="")
            time.sleep(1)
            print(col.Fore.RESET,cards[randomcard])
            cards.pop(randomcard)                                                            
            return 1
        else:
            print(col.Fore.YELLOW + col.Back.LIGHTWHITE_EX + "Bot passing.")
            reset_colors()
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
    print(col.Fore.GREEN + "User points:",upoints)
    print(col.Fore.RED + "Bot points:",bpoints)