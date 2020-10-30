import time 
import random
import core

cards = [1,2,3,4,5,6,7,8,9,10,11]
ucards = []
bcards = []

bpass = False
upass = False

upoints = 0
bpoints = 0

end = False
ready = False

while end == False:
    cards = [1,2,3,4,5,6,7,8,9,10,11]
    bpass = False
    upass = False
    ready = False
    ucards = []
    bcards = []
    core.firstmix(cards,ucards,bcards)

    core.showdown(upoints,bpoints)

    while ready == False:
        mbcards = bcards.copy()
        mbcards.pop(0)
        upass = core.user_turn(cards,ucards,mbcards)

        mucards = ucards.copy()
        mucards.pop(0)
        bpass = core.bot_turn(cards,bcards,mucards)

        if (core.check_pass(upass,bpass) == 1):
            winner = core.match_results(ucards,bcards)
            utotal = core.count_total(ucards)
            btotal = core.count_total(bcards)
            print("Winner is:",end="")
            time.sleep(2)
            if (winner == 1):
                print("user!")
                upoints+=1
            if (winner == 2):
                print("bot!")
                bpoints+=1
            print(utotal,"//",btotal)
            ready = True
            