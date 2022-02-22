from card_ml.cards import Card, Order, Suit


if __name__ == "__main__":
    card = Card(Order.ACE, Suit.SPADES)
    print(card)
