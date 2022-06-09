import random
class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['H', 'D', 'C', 'S']
    
    def __init__(self):
        self.cards = []
        self.fill_deck()
        
    def fill_deck(self):
        for i in self.values:
            for j in self.suits:
                self.cards.append(f"{i}{j}")
    
    def shuffle(self):    
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)


    def deal(self, n):
        dealt_cards = []
        for i in range(n):
            if len(self.cards) == 0:
                break
            card = self.cards.pop()
            dealt_cards.append(card)

        return dealt_cards

    def sort_by_suit(self):
        # to sort cards, turn it into a dictionary
        cards_by_suit = {"H": [], "D": [], "C": [], "S": []}

        for card in self.cards:
            suit = card[-1]
            cards_by_suit[suit].append(card)
        
        self.cards = (
            cards_by_suit["H"] +
            cards_by_suit["D"] +
            cards_by_suit["C"] +
            cards_by_suit["S"] 
        )

    
    def get_cards(self):
        return self.cards[:]

    def contains(self, card):
        if card in self.cards:
            return True
        else:
            return False

    def copy(self):
        deck_copy = Deck()
        deck_copy.cards = self.cards[:]
        return deck_copy


d = Deck()
d.shuffle()
d.deal(2)
d.deal(2)
d.deal(2)
len(d)
d.contains("AH")
