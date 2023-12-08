class Card:
    def __init__(self, hand, bid, rank=0):
        self.hand = hand
        self.bid = bid
        self.rank = rank


"""
Split each line into its own array hands and bid
create an object which has mapping for hand and bid
sort list of those objects by the hand type
make a seperate function to do the sorting
"""

def sort_cards(cards: list[Card]) -> list[Card]:
    pass


def process_game(cards: list[Card]) -> int:
    cards = sort_cards(cards)


if __name__ == "__main__":
    cards: list[Card] = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            hand, bid = line.strip().split(" ")
            cards.append(Card(hand=hand, bid=bid))

    for card in cards:
        print(f"card.hand: {card.hand}, card.bid: {card.bid}, card.rank: {card.rank}")
