#Don't pass without odds
import random
bank = 0
point = 0
numRolls = 5000000
for x in range(1,numRolls + 1):
    roll = random.randrange(1,7) + random.randrange(1,7)
    if point == 0:
        if roll == 7 or roll == 11: bank -= 10
        elif roll == 2 or roll == 3: bank += 10 
        elif roll in range (4,11): point = roll
    elif roll == 7: 
        bank += 10
        point = 0
    elif roll == point:
        bank -= 10
        point = 0
print(bank/numRolls)

#Don't pass with 3x odds
import random
bank = 0
point = 0
numRolls = 1000000
for x in range(1,numRolls + 1):
    roll = random.randrange(1,7) + random.randrange(1,7)
    if point == 0:
        if roll == 7 or roll == 11: bank -= 10
        elif roll == 2 or roll == 3: bank += 10 
        elif roll in range (4,11): point = roll
    elif roll == 7:
        if point ==4 or point == 10:bank += 25
        if point == 5 or point == 9: bank += 30
        if point == 6 or point ==8: bank +=35
        point = 0
    elif roll == point:
        bank -= 40
        point = 0
print(bank/numRolls)

#Don't pass with odds and a $12 place bet on 6
import random
bank = 0
point = 0
numRolls = 10000000
for x in range(1,numRolls + 1):
    roll = random.randrange(1,7) + random.randrange(1,7)
    if point != 0 and roll == 6: bank += 14
    if point == 0:
        if roll == 7 or roll == 11: bank -= 10
        elif roll == 2 or roll == 3: bank += 10 
        elif roll in range (4,11): point = roll
    elif roll == 7:
        #We always made a pass bet on 6, so we win 12 less here 
        if point ==4 or point == 10:bank += 13
        if point == 5 or point == 9: bank += 18
        if point == 6 or point ==8: bank += 23
        point = 0
    elif roll == point:
        bank -= 40
        point = 0

print(bank/numRolls)
