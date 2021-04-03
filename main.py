import random
import craps
# import Classes.GlobalVars as gv
# import Classes.Odds as odds
import settings as s
printblock = 'print("step:",step,"round:",s._rounds,"purse:",s._purse,"die1:",die1,"die2:",die2,"roll:",roll,"hard:",s._hard)'

while s._rounds >0:
    s._passline = 0
    s._bpassline = s._bet*2
    s._hardbets = 0
    s._hard = 0
    s._passline += s._bet
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    roll = die1+die2
    point = craps.point(roll)
    if point == 1: Point = roll
    step = 1
    exec(printblock)
    while point ==1:
        step = 2
        exec(printblock)
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll = die1+die2
        hard = (1 if die1==die2 else 0)
        if ((roll==4) or (roll==5) or (roll==6) or (roll==8) or (roll==9) or (roll==10) or (roll==7)):
            s._purse += ((s._passline+(s._passline*s._bpassline410odds)+s._passline) if (roll==4) or (roll==10) else 0)
            s._purse += ((s._passline+(s._passline*s._bpassline59odds)+s._passline) if (roll==5) or (roll==9) else 0)
            s._purse += ((s._passline+(s._passline*s._bpassline68odds)+s._passline) if (roll==6) or (roll==8) else 0)
            s._purse -= (s._passline+s._bpassline if (roll==7) else 0)
            point = 0
        step = 3
        exec(printblock)

    s._purse += (s._passline if (roll ==7) or (roll ==11) else 0)
    s._purse -= (s._passline if (roll ==2) or (roll ==3) or (roll ==12) else 0)
    step = 4
    exec(printblock)
    s._rounds -=1


