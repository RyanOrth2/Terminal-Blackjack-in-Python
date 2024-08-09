import random

from blackjack import printGame



class Card:


    def __init__(self, number, value):
        self.number = number
        if number > 10:
            self.value = 10
        else:
            self.value = number

    def numToCard(self):
        if self.number == 10:
            return '10'
        
        retVal = ''

        if self.number == 13:
            retVal += 'K '
        elif self.number == 12:
            retVal += 'Q '
        elif self.number == 11:
            retVal += 'J '
        elif self.number == 1:
            retVal += 'A '
        else:
            retVal += str(self.number) + ' '

        return retVal


class Hand:


    def __call__(self):
        return Hand

    def __init__(self):
        self.cards = []


    def __print__(self):
        for x in self.cards:
            print(".------.", end = " ")
        print('')
        for x in self.cards:
            print("|" + Card.numToCard(x) + "/\\  |", end = " ")
        print('')
        for x in self.cards:
            print("| /  \\ |", end = " ")
        print('')
        for x in self.cards:
            print("| \\  / |", end = " ")
        print('')
        for x in self.cards:
            print("|  \\/" + Card.numToCard(x) + "|", end = " ")
        print('')
        for x in self.cards:
            print("'------'", end = " ")
        print('')

    
    def sum(self):
        sum = 0
        for x in self.cards:
            sum += x.value

        for x in self.cards:
            if x.number == 1 and sum < 12:
                sum += 10

        return sum


    def add(self):
        temp = random.randint(1, 13)
        self.cards.append(Card(temp, temp))

    def clear(self):
        self.cards.clear()

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
