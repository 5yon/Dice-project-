import random

def diceroll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def Double():
    return random.randint(1, 6)

def main():
    rounds = 1
    while rounds <= 5:
        print("Round", rounds)
        player1_score = 0
        player2_score = 0
        player1_double = False
        player2_double = False


        print("Player 1's turn:")
        while True:
            player1_dice = diceroll()
            print("Player 1, you rolled:", player1_dice)
            if player1_dice[0] == player1_dice[1]:
                print("If you rolled a double, you recieve another go!")
                player1_double = True
            player1_score += player1_dice[0] + player1_dice[1]
            if not player1_double:
                break
            player1_double = False


        print("Player 2's turn:")
        while True:
            player2_dice = diceroll()
            print("Player 2, you rolled:", player2_dice)
            if player2_dice[0] == player2_dice[1]:
                print("If you rolled a double, you recieve another go!")
                player2_double = True
            player2_score += player2_dice[0] + player2_dice[1]
            if not player2_double:
                break
            player2_double = False


        print("Player 1's score:", player1_score)
        print("Player 2's score:", player2_score)
        if player1_score % 2 == 0:
            print("Player 1, you get 10 points.")
            player1_score += 10
        else:
            print("Player 1, you lose 5 points.")
            player1_score -= 5
        if player2_score % 2 == 0:
            print("Player 2, you get 10 points.")
            player2_score += 10
        else:
            print("Player 2, you lose 5 points.")
            player2_score -= 5


        if player1_score > player2_score:
            print("Player 1 wins the round")
        elif player1_score < player2_score:
            print("Player 2 wins the round")
        else:
            print("The round is a tie")
        print()

        rounds += 1


    if player1_score > player2_score:
        print("Player 1 wins the game")
    elif player1_score < player2_score:
        print("Player 2 wins the game")
    else:
        print("The game is a tie")

main()
