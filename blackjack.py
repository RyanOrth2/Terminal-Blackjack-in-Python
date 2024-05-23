import random
import os
from art import *


def clear():
    os.system('cls')


def printHand(hand):
    for x in hand:
        print(".------.", end = " ")
    print('')
    for x in hand:
        print("|" + numToCard(x) + "/\\  |", end = " ")
    print('')
    for x in hand:
        print("| /  \\ |", end = " ")
    print('')
    for x in hand:
        print("| \\  / |", end = " ")
    print('')
    for x in hand:
        print("|  \\/" + numToCard(x) + "|", end = " ")
    print('')
    for x in hand:
        print("'------'", end = " ")
    print('')


def numToCard(x):
    if x == 10:
        return '10'
    
    retVal = ''

    if x == 13:
        retVal += 'K '
    elif x == 12:
        retVal += 'Q '
    elif x == 11:
        retVal += 'J '
    elif x == 1:
        retVal += 'A '
    else:
        retVal += str(x) + ' '

    return retVal


def hit(hand):
    hand.append(random.randint(1, 13))


def deal(player, dealer):
    player.clear()
    dealer.clear()

    player.append(random.randint(1,13))
    dealer.append(random.randint(1,13))
    player.append(random.randint(1,13))


player = []
dealer = []

print(logo)
print('\n\n\n\n\n')

print('Welcome to Terminal Blackjack!\n\nWould you like to play?')