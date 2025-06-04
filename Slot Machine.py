import time
import random
import pygame
#This "spins" the slot machine randomly
def spin_row():
    symbols = ["🍎", "⭐️", "🫐"]
    results = []
    for emoji in range(3):
        results.append(random.choice(symbols))
    return results
#This function prints the outline and emojis after spinning.
def print_row(row):
    print("----------------------")
    print("   |   ".join(row), end=" |   ")
    print("")
    print("----------------------")
    print("")
#This function checks to see if the values in the appended list match each other for a win.
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🫐":
            outcome = "YOU WIN!"
            for i in outcome:
                print(i, end= " ")
                time.sleep(.21)
            print()
            return bet * 10, outcome
        elif row[0] == "🍎":
            outcome = "YOU WIN!"
            for i in outcome:
                print(i, end=" ")
                time.sleep(.21)
            print()
            return bet * 12, outcome
        elif row[0] == "⭐️":
            outcome = "JACKPOT!"
            for i in outcome:
                print(i, end=" ")
                time.sleep(.21)
            print()
            return bet * 20, outcome
    return 0, "YOU LOSE!"
#This is the main function that calls every other function it asks you to play again and place your bet
def main_function():
    balance = 100
    highest_payouts = []

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("$$$-WELCOME TO PYTHON SLOTS-$$$")
    print("$$$-SLOT SYMBOLS:🫐  🍎  ⭐️-$$$")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while balance > 0:
        print(f"\nCURRENT BALANCE: ${balance}")

        bet = input("Place your bet amount: $")
        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <=0:
            print("Bet must be greater than 0")


        balance -= bet


        row = spin_row()
        print("\nMAY THE ODDS BE IN YOUR FAVOR")
        pygame.mixer.init()
        sound = pygame.mixer.Sound("Slot Machine Pull 1 - QuickSounds.com.mp3")
        sound.play()
        for spin in range(3):
            time.sleep(.2)
            spinning = "spin..."
            for letter in spinning:
                print(letter, end=' ')
                time.sleep(.27)
            print()

        print("S T O P !")
        print("")

        print_row(row)

        payout, outcome = get_payout(row, bet)

        if payout > 0:
            pygame.mixer.init()
            sound = pygame.mixer.Sound("Slot-winning-chimes-2015.wav")
            sound.play()
            print(f"You won: ${payout}")
            print("")
            highest_payouts.append(payout)
            highest_payouts = sorted(highest_payouts, reverse=True)[:3]

        else:
            pygame.mixer.init()
            sound = pygame.mixer.Sound("Slot-retro-arcade-game-over-470.wav")
            sound.play()
            print(f"Sorry you lost: ${bet}")
            print("")

        balance += payout

        play_again = input("Do you want to play again (Y|N)? ").upper()

        if play_again == "Y" and balance > 0:
            continue
        elif play_again == "Y" and balance == 0:
            print("\nUnfortunately you are out of funds. Thank you for playing!")
            for i in highest_payouts:
                print("\nHIGHEST PAYOUT LEADERBOARD: ")
                print(f"${i}", sep=" ")
        elif play_again == "N":
            print(f"\nThank you for playing! Your payout is ${balance}")
            balance = 0
            for i in highest_payouts:
                print("\nHIGHEST PAYOUT LEADERBOARD: ")
                print(f"${i}", sep=" ")

if __name__ == "__main__":
    main_function()