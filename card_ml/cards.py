from dataclasses import dataclass
from enum import Enum


class Suit(Enum):
    HEARTS = "hearts"
    SPADES = "spades"
    CLUBS = "clubs"
    DIAMONDS = "diamonds"


class Order(Enum):
    ACE = "ace"
    TWO = "two"
    THREE = "three"
    FOUR = "four"
    FIVE = "five"
    SIX = "six"
    SEVEN = "seven"
    EIGHT = "eight"
    NINE = "nine"
    TEN = "ten"
    JACK = "jack"
    QUEEN = "queen"
    KING = "king"


@dataclass
class Card:
    order: Order
    suit: Suit

    def __str__(self) -> str:
        return f"{self.order} of {self.suit}"
