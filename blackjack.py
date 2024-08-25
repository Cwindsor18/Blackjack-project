import random 

class Deck: 
    def __init__(self):
        ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        suites = ["H","D","S","C"]
        self.cards = [[suite,rank]for rank in ranks for suite in suites]
        random.shuffle(self.cards)
    def deal(self): 
        return self.cards.pop() 
    
class Hand: 
    def __init__(self,deck): 
        self.hand = []
    def add_card(self,deck):
        self.hand.append(deck.deal())
    def print_hand(self): 
        print(self.hand)

class Player_Hand: 
    def __init__(self,deck): 
        self.total = 0 
        self.hand = Hand(deck)
        self.hand.add_card(deck)
        self.hand.add_card(deck) 
    def print_hand(self): 
        self.hand.print_hand() 
    def total_hand(self):
        self.total = 0 
        num_aces = 0 
        for card in self.hand.hand: 
            rank = card[1] 
            if rank in ["J","Q","K"]: 
                self.total+= 10 
            elif rank == "A":
                num_aces+= 1 
                self.total+= 11
            else: 
                self.total+= int(rank)
        while self.total > 21 and num_aces > 0: 
            self.total-= 10 
            num_aces -= 1
        return self.total 
    
class Dealer: 
    def __init__(self,deck): 
        self.total = 0
        self.hand = Hand(deck)
        self.hand.add_card(deck)
        self.hand.add_card(deck)
        print(self.hand.hand[0])
    def print_hand(self): 
        self.hand.print_hand() 
    def total_hand(self):
        self.total = 0 
        num_aces = 0 
        for card in self.hand.hand: 
            rank = card[1] 
            if rank in ["J","Q","K"]: 
                self.total+= 10 
            elif rank == "A":
                num_aces+= 1 
                self.total+= 11
            else: 
                self.total+= int(rank)
        while self.total > 21 and num_aces > 0: 
            self.total-= 10 
            num_aces -= 1
        return self.total 
            
        
        
        

      
def main ():
    while True:
        deck = Deck()
        print("Dealer's Hand:")
        dealer = Dealer(deck)
        dealer.total_hand()
        player = Player_Hand(deck)
        print("Player's Hand:")
        player.total_hand()
        player.print_hand()
        while True: 
            choice = input("Hit me or Stand (h/s) ").lower()
            if choice == "h": 
                player.hand.add_card(deck)
                player.total_hand()
                player.print_hand()
                if player.total > 21: 
                    print("You Lose!")
                    break 
            elif choice == "s": 
                dealer.total_hand()
                while dealer.total < 18: 
                    dealer.hand.add_card(deck)
                    dealer.total_hand()
                print("Dealer's Hand:")
                dealer.print_hand()
                if dealer.total > 21: 
                    print("You Win!")
                elif dealer.total > player.total: 
                    print("You lose!")
                elif dealer.total < player.total: 
                    print("You Win!")
                else: 
                    print("Tie")
                break 
            else: 
                print("Please choose h or s")
        play_again = input("Play again? y/n: ").lower()
        if play_again != "y": 
            break 
        
                    

    
    
    


    
    
    #x=0
    #pointer = 1
   # Hand = []
   # Hand.append(deal())
    # Hand.append(deal())
    # Dealer = [] 
    # Dealer.append(deal())
    # if Dealer[0] == Face_Card.A.name: 
    #     Dealer[0] = 11
    # print("Welcome to Blackjack")
    # print("Here's your hand")
    # print(Hand)
    # if Hand[0]== Face_Card.A.name: 
    #     userplayer = input("I see that you have aquired an A. Do you to make it 1 or 11? Type 1 or 11 \n")
    #     if userplayer == ("1"):
    #         Hand[0] = 1
    #     elif userplayer == ("11"): 
    #         Hand[0] = 11
    #     print("Here's your new Hand" , Hand )
    # if Hand[1] == Face_Card.A.name: 
    #     userplayer = input("I see that you have aquired an A. Do you to make it 1 or 11? Type 1 or 11 \n")
    #     if userplayer == ("1"):
    #         Hand[1] = 1
    #     elif userplayer == ("11"): 
    #         Hand[1] = 11
    #     print("Here's your new Hand" , Hand )
    # print("Here's your dealer's hand \n" , Dealer[0])
    
    # while x != -1: 
    #     userplayer = input("Hit me or Stand: \n") 
                
    #     if sum(Hand) == 21: 
    #         print("YOU WIN. Thank you for playing!")
    #         break 
        
    #     if userplayer.upper() == "HIT ME": 
    #         Hand.append(deal())
    #         pointer+= 1
    #         print("Here's your hand" , Hand)
    #         if Hand[pointer]== Face_Card.A.name: 
    #             userplayer = input("I see that you have aquired an A. Do you to make it 1 or 11? Type 1 or 11 \n")
    #             if userplayer == ("1"):
    #                 Hand[pointer] = 1
    #             elif userplayer == ("11"): 
    #                 Hand[pointer] = 11
    #             print("Here's your new Hand" , Hand )
                
    #         if sum(Hand) > 21: 
    #             print("YOU LOSE. Thank you for playing!")
    #             break 
    #         if sum(Hand) == 21: 
    #             print("YOU WIN. Thank you for playing!")
    #             break
    #     elif userplayer.upper() == "STAND":
    #         Dealer.append(deal())
    #         if Dealer[1] == Face_Card.A.name: 
    #             Dealer[1] = 11
    #         print("Here's is the Dealer's Hand" , Dealer) 
    #         if sum(Dealer) < sum(Hand): 
    #             print("YOU WIN. Thank you for playing!")
    #             break 
    #         if sum(Dealer) == sum(Hand): 
    #             print("Draw. Go home!") 
    #             break
    #         if sum(Dealer) > sum(Hand):
    #              print("YOU LOSE. Thank you for playing!")
    #              break
            
    
if __name__ == "__main__":
     main()
    
        