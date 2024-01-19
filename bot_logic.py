import random


def generate_hand():
    hand_gesture = ["Rock", "Paper", "Scissors"]
    number_generated = random.randint(0, 2)
    result = hand_gesture[number_generated]

    return [number_generated, result]
