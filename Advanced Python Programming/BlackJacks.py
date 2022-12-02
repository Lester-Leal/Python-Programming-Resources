# Black Jack Game - Play a game of Black Jack
# Author: Lester Leal

# import the random module
import random

# define the main function
def main():
    # initialize the player's and dealer's hands
    playerHand = []
    dealerHand = []

    # deal the player's and dealer's first cards
    deal(playerHand)
    deal(dealerHand)
    deal(playerHand)
    deal(dealerHand)

    # display the player's and dealer's hands
    print("Player's hand:", playerHand)
    print("Dealer's hand:", dealerHand)

    # initialize the player's and dealer's scores
    playerScore = getScore(playerHand)
    dealerScore = getScore(dealerHand)

    # initialize the player's turn
    playerTurn = True

    # loop until the player's and dealer's scores are less than 21
    while playerScore < 21 and dealerScore < 21:
        # if it is the player's turn
        if playerTurn:
            # get the player's choice
            choice = input("Do you want to hit or stay? ")

            # if the player wants to hit
            if choice.lower() == "hit":
                # deal the player another card
                deal(playerHand)

                # display the player's hand
                print("Player's hand:", playerHand)

                # get the player's score
                playerScore = getScore(playerHand)
            else:
                # set the player's turn to false
                playerTurn = False
        else:
            # if the dealer's score is less than 17
            if dealerScore < 17:
                # deal the dealer another card
                deal(dealerHand)

                # display the dealer's hand
                print("Dealer's hand:", dealerHand)

                # get the dealer's score
                dealerScore = getScore(dealerHand)
            else:
                # set the player's turn to true
                playerTurn = True

    # if the player's score is greater than 21
    if playerScore > 21:
        # display the dealer's hand
        print("Dealer's hand:", dealerHand)

        # display the dealer's score
        print("Dealer's score:", dealerScore)

        # display the player's score
        print("Player's score:", playerScore)

        # display the dealer wins message
        print("Dealer wins!")
    # if the dealer's score is greater than 21
    elif dealerScore > 21:
        # display the player's hand
        print("Player's hand:", playerHand)

        # display the player's score
        print("Player's score:", playerScore)

        # display the dealer's score
        print("Dealer's score:", dealerScore)

        # display the player wins message
        print("Player wins!")

    # if the player's score is greater than the dealer's score
    elif playerScore > dealerScore:
        # display the player's hand
        print("Player's hand:", playerHand)

        # display the player's score
        print("Player's score:", playerScore)

        # display the dealer's score
        print("Dealer's score:", dealerScore)

        # display the player wins message
        print("Player wins!")
    # if the dealer's score is greater than the player's score
    elif dealerScore > playerScore:
        # display the dealer's hand
        print("Dealer's hand:", dealerHand)

        # display the dealer's score
        print("Dealer's score:", dealerScore)

        # display the player's score
        print("Player's score:", playerScore)

        # display the dealer wins message
        print("Dealer wins!")
    # if the player's score is equal to the dealer's score
    else:
        # display the player's hand
        print("Player's hand:", playerHand)

        # display the player's score
        print("Player's score:", playerScore)

        # display the dealer's hand
        print("Dealer's hand:", dealerHand)

        # display the dealer's score
        print("Dealer's score:", dealerScore)

        # display the tie message
        print("It's a tie!")

# define the deal function
def deal(hand):
    # get a random card
    card = random.randrange(1, 14)

    # if the card is a face card
    if card > 10:
        # set the card to 10
        card = 10

    # add the card to the hand
    hand.append(card)

# define the getScore function
def getScore(hand):
    # initialize the score
    score = 0

    # loop through the hand
    for card in hand:
        # add the card to the score
        score += card

    # return the score
    return score

main()
