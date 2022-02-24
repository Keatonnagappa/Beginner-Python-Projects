import random
from tkinter import Y

# Dealing functionality


def deal():
    """Returns random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Calculating scores


def calculate_score(cards):
    """Take the list of cards and calculate the score based on said cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Comparing score to determine the outcome of the match


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "You lose, Deal has Blackjack"
    elif user_score == 0:
        return "You win with Blackjack!"
    elif user_score > 21:
        return "You went over 21, you lose"
    elif dealer_score > 21:
        return "Dealer went over 21, you win!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You Lose!"


def play_game():
    # Starting cards for user and dealer
    user_cards = []
    dealer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal())
        dealer_cards.append(deal())

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's card: {dealer_cards[0]}")

        # Conditional Statments to continue or end game

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            continue_dealing = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
            if continue_dealing == "y":
                user_cards.append(deal())
            else:
                game_over = True

    # Conditional for the dealer to continue deal cards for themself
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your Final hand: {user_cards},final score was {user_score}")
    print(
        f"Dealer's Final hand: {dealer_cards},final score was {dealer_score}")
    print(compare(user_score, dealer_score))


while input("Do you want to play a game of Blackjack? y or n ") == "y":
    play_game()
