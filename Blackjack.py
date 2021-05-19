from random import randint
from IPython.display import clear_output


class Game():
    def __init__(self):
        self.deck=[]
        self.suits=("Spades","Diamond","Heart","Clubs")
        self.values=(2,3,4,5,6,7,8,9,10,'J','Q','K','A')


    def makeDeck(self):
        for i in self.values:
            for j in self.suits:
                self.deck.append((i,j))

    def pullCard(self):
        return self.deck.pop(randint(0,len(self.deck)-1))


class Player():
    def __init__(self,name):
        self.name=name
        self.hand=[]

    def addCard(self,card):
        self.hand.append(card)

    def showHand(self,dealer_start=True):
        print(f"\n{self.name}")
        print("=============")
        for i in range(len(self.hand)):
            if self.name=="Dealer" and i==0 and dealer_start:
                print("- of -")
            else:
                card=self.hand[i]
                print(f"{card[0]} of {card[1]}")


    def calchand(self,dealers_start=True):
        total=0
        aces=0
        cardvalues={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':10,'Q':10,'K':10,'A':11}
        if self.name=="Dealer" and dealers_start:
            card=self.hand[1]
            return cardvalues[card[0]]
        for card in self.hand:
            # print("Card ",card[0])
            if card[0]=='A':
                aces+=1
            else:
                total+=cardvalues[card[0]]
        for i in range(aces):
            if total + 11 > 21:
                total +=1
                # print(self.name," total +1 = ", total)
            else:
                total +=11
                # print(self.name," total +11 = ", total)
        # print("Total = ",total)

        return total


x=Game()
x.makeDeck()
# print(x.deck)
# print(x.pullCard())

player=Player(input("Enter your name\n"))
dealer=Player("Dealer")
# print(player.name,dealer.name)
for i in range(2):
    player.addCard(x.pullCard())
    dealer.addCard(x.pullCard())
# print(f"Player hands : {player.hand} \nDealer hands : {dealer.hand}")
player.showHand()
dealer.showHand()
playerburst=False
while(input("Would you like to stay of hit").lower()!="stay"):
    clear_output()
    player.addCard(x.pullCard())
    player.showHand()
    dealer.showHand()
    if player.calchand()>21:
        playerburst=True
        break

dealerburst=False
if not dealerburst:
    while dealer.calchand(False)<17:
        dealer.addCard(x.pullCard())
        if dealer.calchand(False)>21:
            dealerburst=True
            break

clear_output()
player.showHand()
dealer.showHand(False)
if playerburst:
    print("You bursted! Better luck next time\n")
elif dealerburst:
    print("Dealer Burst! You win\n")
elif dealer.calchand(False)>player.calchand():
    print("Dealer has higher card, you lose!\n")
elif dealer.calchand(False)<player.calchand():
    print("You beat dealer,You win!!\n")
else:
    print("You pushed,no one wins!\n")

print("Total of player = ", player.calchand())
print("Total of dealer = ", dealer.calchand(False))
