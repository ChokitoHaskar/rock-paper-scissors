from random import SystemRandom

hands = {
    1: "✊",
    2: "✋",
    3: "✌",
}


# Computer AI
def bot_ai():
    return SystemRandom().randint(1, 3)


print("\n🎊 Welcome to the game of simple ✊ Rock ✋ Paper ✌ Scissors!! 🎊\n")

game_state = True

while game_state:
    print("1. ✊\n2. ✋\n3. ✌\n0. 👋")
    try:
        user = int(input("Select your hand:\n"))
    except ValueError:
        print(
            "\nIt seems your input is not an integer number\nPlease, try input a number instead\n"
        )
        continue
    if user == 0:
        print("\nBye-Bye 👋\n")
        game_state = False

    elif user > 3 or user < 0:
        print(
            "\nIt seems your input is not included in the available option\nPlease try again.\n"
        )
        continue

    else:
        bot = bot_ai()
        print(f"\nPlayer {hands[user]} against Computer {hands[bot]}")
        if user == bot:
            print("It's a Draw!!\n")

        else:
            if (
                (user == 1 and bot == 2)
                or (user == 2 and bot == 3)
                or (user == 3 and bot == 1)
            ):
                print("Computer Wins!!\n")
            else:
                print("Player Wins!!\n")
