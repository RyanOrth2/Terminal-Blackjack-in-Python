import random
import os
import time
from art import *
from helper_functions import Hand, Card


def clear():
    os.system('cls')


def printGame(player, dealer):
    Hand.__print__(dealer)
    print('\n\n\n\n\n')
    Hand.__print__(player)


def hit(person):
    Hand.add(person)


def deal(player, dealer):
    player.clear()
    dealer.clear()

    Hand.add(player)
    Hand.add(dealer)
    Hand.add(player)


    def playRound(self, player, dealer):
        while player.sum() < 22 and (playerIn != 'st' or playerIn != 'q'):
            printGame(player, dealer)
            print("\nYou have ", end = " ")
            print(player.sum(), end = " ")
            print("against the Dealers' ", end = " ")
            print(dealer.sum())

            if player.sum() < 21:
                playerIn = input("\nWhat would you like to do?\t(h)it / (st)and / (d)ouble / (sp)lit / (q)uit\n")

                while playerIn != 'h' and playerIn != 'st' and playerIn != 'd' and playerIn != 'sp' and playerIn != 'q':
                    playerIn = input("\nSorry, we didn\'t recognize that one...\n\nWhat would you like to do?\t(h)it / (st)and / (d)ouble / (sp)lit / (q)uit\n")

                match (playerIn):
                    case "h":
                        player.add()
                    case "st":
                        continue
                    case "d":
                        player.add()
                        playerIn = "st"


player = Hand()
dealer = Hand()
playerIn = 'z'
gameIn = 'z'

print(logo)
time.sleep(3)
print('\n\n\n\n\n')

gameIn = input('Welcome to Terminal Blackjack!\n\nWould you like to play?    (y/n)\n\n')

while gameIn != 'y' and gameIn != 'n':
    gameIn = input('\nSorry, we didn\'t recognize that one...\n\nWould you like to play?    (y/n)\n\n')

if gameIn == 'n':
    exit(1)

print("\n\nRight on! We'll deal you in!")
time.sleep(3) 
clear()
deal(player, dealer)


while gameIn != 'q':

    
    



    userIn = input("Would you like to play again?   (y/n)\n\n")
    
    while userIn != 'y' and userIn != 'n':
        userIn = input('\nSorry, we didn\'t recognize that one...\n\nWould you like to play again?    (y/n)\n\n')

    if userIn == 'n':
        print('\n\nSee you next time!')
        exit(1)
