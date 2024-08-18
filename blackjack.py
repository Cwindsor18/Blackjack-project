import random 
import math 
from enum import Enum 

class Face_Card (Enum):
    J = 10
    Q = 10
    K = 10
    A = 0
DECKSIZE = 52
deck = [DECKSIZE]

deck = [Face_Card.A.name,Face_Card.A.name,Face_Card.A.name,Face_Card.A.name,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,Face_Card.J.value,Face_Card.J.value,Face_Card.J.value,Face_Card.J.value,Face_Card.Q.value,Face_Card.Q.value,Face_Card.Q.value,Face_Card.Q.value,Face_Card.K.value,Face_Card.K.value,Face_Card.K.value,Face_Card.K.value]



def deal ():
  random_integer = random.randint(0, len(deck) - 1)
  dealtCard = deck.pop(random_integer)
  return dealtCard

      
      
def main ():
    x=0
    pointer = 1
    Hand = []
    Hand.append(deal())
    Hand.append(deal())
    Dealer = [] 
    Dealer.append(deal())
    if Dealer[0] == Face_Card.A.name: 
        Dealer[0] = 11
    print("Welcome to Blackjack")
    print("Here's your hand")
    print(Hand)
    if Hand[0]== Face_Card.A.name: 
        userplayer = input("I see that you have aquired an A. Do you to make it 1 or 11? Type 1 or 11 \n")
        if userplayer == ("1"):
            Hand[0] = 1
        elif userplayer == ("11"): 
            Hand[0] = 11
        print("Here's your new Hand" , Hand )
    if Hand[1] == Face_Card.A.name: 
        userplayer = input("I see that you have aquired an A. Do you to make it 1 or 11? Type 1 or 11 \n")
        if userplayer == ("1"):
            Hand[1] = 1
        elif userplayer == ("11"): 
            Hand[1] = 11
        print("Here's your new Hand" , Hand )
    print("Here's your dealer's hand \n" , Dealer[0])
    
    while x != -1: 
        userplayer = input("Hit me or Stand: \n") 
                
        if sum(Hand) == 21: 
            print("YOU WIN. Thank you for playing!")
            break 
        
        if userplayer.upper() == "HIT ME": 
            Hand.append(deal())
            pointer+= 1
            print("Here's your hand" , Hand)
            if Hand[pointer]== Face_Card.A.name: 
                userplayer = input("I see that you have aquired an A. Do you to make it 1 or 11? Type 1 or 11 \n")
                if userplayer == ("1"):
                    Hand[pointer] = 1
                elif userplayer == ("11"): 
                    Hand[pointer] = 11
                print("Here's your new Hand" , Hand )
                
            if sum(Hand) > 21: 
                print("YOU LOSE. Thank you for playing!")
                break 
            if sum(Hand) == 21: 
                print("YOU WIN. Thank you for playing!")
                break
        elif userplayer.upper() == "STAND":
            Dealer.append(deal())
            if Dealer[1] == Face_Card.A.name: 
                Dealer[1] = 11
            print("Here's is the Dealer's Hand" , Dealer) 
            if sum(Dealer) < sum(Hand): 
                print("YOU WIN. Thank you for playing!")
                break 
            if sum(Dealer) == sum(Hand): 
                print("Draw. Go home!") 
                break
            if sum(Dealer) > sum(Hand):
                 print("YOU LOSE. Thank you for playing!")
                 break
            
    
if __name__ == "__main__":
    main()
    
        