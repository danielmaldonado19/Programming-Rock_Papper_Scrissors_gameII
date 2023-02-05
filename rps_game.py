#ROCK PAPPER SCISSORS

import random

'''
.1.User input his choice
.2.Pc generates its choice randomly
'''

print('ROCK, PAPER, SCISSORS GAME. YOU VS PC')

usr_hand = input("Type your choice:").lower()
pc_choices = ['rock','paper','scissor']
pc_hand = random.choice(pc_choices)


print("Your bet is: ",usr_hand)
print("Pc's bet is: ", pc_hand)

if usr_hand == 'rock':
    if pc_hand == 'paper':
        print('YOU LOSE!')
    elif pc_hand =='scissor':
        print('YOU WIN!')
    else:
        print('DRAW! BOTH WIN.')
        
elif usr_hand == 'paper':
    if pc_hand == 'rock':
        print('YOU WIN!')
    elif pc_hand =='scissor':
        print('YOU LOSE!')
    else:
        print('DRAW! BOTH WIN.')
        
elif usr_hand =='scissor':
    if pc_hand == 'rock':
        print('YOU LOSE!')
    elif pc_hand =='paper':
        print('YOU WIN!')
    else:
        print('DRAW! BOTH WIN.')
    
else: 
    print("Wrong value. Please try again")