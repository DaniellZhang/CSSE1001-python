#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""
# HumanPlayer, ComputerPlayer, Deck, card, SkipCard, ReverseCard, Pickup2Card, Pickup4Card/
# what i need to create
import random

__author__ = "Bosheng Zhang & 45004830"

# Write your classes here
class Card(object):
    """
    a class for managing the basic type of colour and number
    """
    def __init__(self, number, colour):
        """
        Construct a card from the basic type of colour and number

        parameters:
            number (int): The number of the card
            color (string): The color of the card
        """
        self._number = number
        self._colour = colour
        self._match = False
    def get_number(self):
        """
        Returns the card number
        """
        return self._number
    def get_colour(self):
        """
        Returns the card colour
        """
        return self._colour
    def set_number(self, number):
        """
        Set the number value of the card
        
        Parameters:
            number (int): The number of the card
        """
        self._number = number
    def set_colour(self, colour):
        """
        Set the colour of the card
        
        Parameters:
            colour (string): The color of the card
        """
        self._colour = colour
    def get_pickup_amount(self):
        """
        Returns the amount of cards the next player should pickup
        """
        return 0
    def matches(self, card):
        """
        Returns True if the next card to be placed on the pile matches this card.
        "Matches" is defined as being able to be placed on top of this card legally.
        A "match" for the base Card is a card of the same colour or number.

        Parameters:
            card(Card): The card on the top of the deck.
        """
        if self._colour == card._colour or self._number == card._number:
            return True
        else:
            return False
    def play(self, player, game):
        """
        Perform a special card action. The base Card class has no special action.

        Parameters:
            player (Player): The current player.
            game (a2_support.UnoGame): This current uno game
        """
        pass      
    def __str__(self):
        """ Returns the string representation of this card.
        __str__() -> str
        """
        return "Card({0}, {1})".format(self._number, self._colour)
    def __repr__(self):
        return "Card({0}, {1})".format(self._number, self._colour)

class SkipCard(Card):
    """
    A subclass of the Card to manage skipcard function
    """
    def __init__(self, number, colour):
        super().__init__(number, colour)
        self._location = 0
    def matches(self, card):
        """
        Returns True if the next card to be placed on the pile matches this card.
        "Matches" is defined as being able to be placed on top of this card legally.
        A "match" for the base Card is a card of the same colour or number.

        Parameters:
            card(Card): The card on the top of the deck.
        """
        return self._colour == card._colour
    def play(self, player, game):
        """
        (T): Moves onto the next player, skipping 'count' amount players.
        """
        game._turns.skip()
    def __str__(self):
        """ Returns the string representation of this card.
        __str__() -> str
        """
        return "SkipCard({0}, {1})".format(self._number, self._colour)
    def __repr__(self):
        return "SkipCard({0}, {1})".format(self._number, self._colour)
class ReverseCard(Card):
    """
    A subclass of the Card to manage ReverseCard function
    """
    def __init__(self, number, colour):
        super().__init__(number, colour)
    def matches(self, card):
        """
        Returns True if the next card to be placed on the pile matches this card.
        "Matches" is defined as being able to be placed on top of this card legally.
        A "match" for the base Card is a card of the same colour or number.

        Parameters:
            card(Card): The card on the top of the deck.
        """
        return self._colour == card._colour
    def play(self, player, game):
        """
        Reverse the order of turns.
        """
        game._turns.reverse()
    def __str__(self):
        """ Returns the string representation of this card.
        __str__() -> str
        """
        return "ReverseCard({0}, {1})".format(self._number, self._colour)
    def __repr__(self):
        return "ReverseCard({0}, {1})".format(self._number, self._colour)

class Pickup2Card(Card):
    """
    A subclass of the Card to manage Pickup2Card function
    """
    def __init__(self, number, colour):
        super().__init__(number, colour)
    def play(self, player, game):
        """
        The next player should pick up 2 cards after pickup2Card.

        Parameters:
            player (Player): The current player.
            game (a2_support.UnoGame): This current uno game
        """
        cards = game.pickup_pile.pick(2)[::-1]
        next_player = game.get_turns().peak(1)
        deck = next_player.get_deck()
        deck.add_cards(cards)
    def matches(self, card):
        """
        Returns True if the next card to be placed on the pile matches this card.
        "Matches" is defined as being able to be placed on top of this card legally.
        A "match" for the base Card is a card of the same colour or number.

        Parameters:
            card(Card): The card on the top of the deck.
        """
        return self._colour == card._colour
    def get_pickup_amount(self):
        """
        The next player should pick up 2 cards after pickup2Card
        """
        return 2
    def __str__(self): 
        """ Returns the string representation of this card.
        __str__() -> str
        """
        return "Pickup2Card({0}, {1})".format(self._number, self._colour)
    def __repr__(self):
        return "Pickup2Card({0}, {1})".format(self._number, self._colour)
class Pickup4Card(Card):
    """
    A subclass of the Card to manage Pickup4Card function
    """
    def __init__(self, number, colour):
        super().__init__(number, colour)
    def play(self, player, game):
        """
        The next player should pick up 2 cards after pickup2Card.
        
        Parameters:
            player (Player): The current player.
            game (a2_support.UnoGame): This current uno game
        """
        cards = game.pickup_pile.pick(4)[::-1]
        next_player = game.get_turns().peak(1)
        deck = next_player.get_deck()
        deck.add_cards(cards)
    def matches(self, card):
        """
        Returns True if the next card to be placed on the pile matches this card.
        "Matches" is defined as being able to be placed on top of this card legally.
        A "match" for the base Card is a card of the same colour or number.

        Parameters:
            card(Card): The card on the top of the deck.
        """
        return True
    def get_pickup_amount(self):
        """
        The next player should pick up 4 cards after pickup4Card
        """
        return 4
    def __str__(self):
        """ Returns the string representation of this card.
        __str__() -> str
        """
        return "Pickup4Card({0}, {1})".format(self._number, self._colour)
    def __repr__(self):
        return "Pickup4Card({0}, {1})".format(self._number, self._colour)
class Deck(object):
    """
    A class to manage the deck
    """
    def __init__(self, starting_cards=None):
        """
        Construct a deck with zero startig cards

        Parameters:
            starting_cards: The starting cards of the deck
        """
        if starting_cards == None:
            starting_cards = []
        self.deck_cards = starting_cards
    def get_cards(self):
        """
        Returns a list of cards in the deck.
        """
        return self.deck_cards
    def get_amount(self):
        """
        Returns a list of cards in the deck.
        """
        return len(self.deck_cards)
    def shuffle(self):
        """
        Shuffle the order of the cards in the deck.
        """
        random.shuffle(self.deck_cards)
    def pick(self, amount: int=1):
        """
        Take the first 'amount' of cards off the deck and return them.

        Parameters:
            amount(int): The amount of cards to pick
        """
        card_amount = self.get_amount()
        if amount > card_amount:
            raise Exception('You pick more cards than the deck has!')
        else:
            return_list = self.deck_cards[:-amount-1:-1]
            self.deck_cards = self.deck_cards[:card_amount - amount]
            return return_list
    def add_card(self, card): 
        """
        Place a card on top of the deck.
        """
        self.deck_cards.append(card)
    def add_cards(self, cards):
        """
        Place a list of cards on top of the deck.
        """
        self.deck_cards.extend(cards)
    def top(self): 
        """
        Peaks at the card on top of the deck and returns it
        or None if the deck is empty.
        """
        if self.get_amount() == 0:
            return None
        else:
            return self.deck_cards[-1]
class Player(object):
    """
    A class to manage game players.
    """
    def __init__(self, name):
        self._name = name
        self._deck = Deck()
    def get_name(self):
        """
        Returns the name of the player.
        """
        return self._name
    def get_deck(self):
        """
        Returns the players deck of cards.
        """
        return self._deck
    def is_playable(self): 
        """
        Returns True iff the players moves aren't automatic.
        """
        raise NotImplementedError('is_playable to be implemented by subclasses')
    def has_won(self):
        """
        Returns True iff the player has an empty deck and has therefore won.
        """
        return self.get_deck().get_amount() == 0
    def pick_card(self, putdown_pile):
        """
        Selects a card to play from the players current deck.

        Parameters:
            putdown_pile (Deck): The putdown_pile of the game
        """
        raise NotImplementedError('is_playable to be implemented by subclasses')
class HumanPlayer(Player):
    """
    A subclass to manage human players.
    """
    def __init__(self, name):
        super().__init__(name)
        self._deck = Deck()
    def is_playable(self):
        """
        human players moves aren't automatic
        """
        return True
    def pick_card(self, putdown_pile):
        """
        Selects a card to play from the players current deck.
        Returns None for non-automated players
        Parameters:
            putdown_pile (Deck): The putdown_pile of the game
        """
        return None

class ComputerPlayer(Player):
    """
    A subclass to manage computer players.
    """
    def __init__(self, name):
        super().__init__(name)
        self._deck = Deck()
    def is_playable(self):
        """
        computer players moves are automatic
        """
        return False
    def pick_card(self, putdown_pile):
        """
        Selects a card to play from the players current deck.
        Returns None when a card cannot be played.
        Parameters:
            putdown_pile (Deck): The putdown_pile of the game
        """
        for card in self.get_deck().get_cards():
            if putdown_pile.top().matches(card):
                self.get_deck().get_cards().remove(card)
                return card
        return None
def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
