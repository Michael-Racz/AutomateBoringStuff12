#Dice Roller
#takes in a string of dice in the form such as 3d6, 5d6
# Format for more than one string is 3d8+2 1d3+1
import re,random
def diceRoll(die_string):
    add_roll = 0
    rollregex = re.compile('([0-9]+)([d])([0-9]+)([+-]+)([0-9]+)')
    my_roll = rollregex.findall(die_string)
    #randint(a,b)
    
    #Each ROLL in my_roll is a tuple
    for roll in my_roll:
        for i in range(int(roll[0])):
            add_roll += random.randint(1,int(roll[2]))
        if roll[3] == '+':
            add_roll += int(roll[4])
        elif roll[3] == '-':
            add_roll -= int(roll[4])

    print(add_roll)
print('Format for one roll is "1d6". "1d6+0" and "1d6" are the same.')
print('Format for more than one roll is "1d6 3d6+1 1d20+2". One space between each roll will do.')
print()
while True:
    print('Enter roll: ')
    response = input()
    if response == 'exit':
        break
    diceRoll(response)
    print()
