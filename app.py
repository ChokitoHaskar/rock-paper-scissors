import bot_logic as ai_choice

hand_gesture = ["Rock", "Paper", "Scissors"]
user = False

while user == False:
    user = int(input("1.Rock  2.Paper  3.Scissors \nChoose your hand(1, 2, or 3)\n"))

    computer = ai_choice.generate_hand()
    # computer[0] is the number
    # computer[1] is the hand_gesture

    if user < 1 or user > 3:
        print("Input choice exceed the desire limit (1 - 3), please try again\n")
        user = False
    else:
        print("\n" + hand_gesture[user - 1] + " against " + computer[1])

        # Player hands : Rock
        if user - 1 == 0:
            if computer[0] == 0:
                print("It's a DRAW\n")
            elif computer[0] == 1:
                print("You WIN\n")
            elif computer[0] == 2:
                print("You LOSE\n")
        # Player hands : Paper
        elif user - 1 == 1:
            if computer[0] == 0:
                print("You WIN\n")
            elif computer[0] == 1:
                print("It's a DRAW\n")
            elif computer[0] == 2:
                print("You LOSE\n")
        # Player hands : Scissors
        elif user - 1 == 2:
            if computer[0] == 0:
                print("You LOSE\n")
            elif computer[0] == 1:
                print("You WIN\n")
            elif computer[0] == 2:
                print("It's a DRAW\n")
