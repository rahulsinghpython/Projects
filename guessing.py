import random

gameset = 1

print("please enter start to begin")

counter = 0

def computerguess():
    global counter
    computer = random.randint(1, 20)
    player_value = input()

    if player_value == "start":
        print("I AM GUESSING IT IS {}".format(computer))

    if player_value == "higher":
        higherComputer = random.randint(computer, 20)
        print("I AM GUESSING IT IS {}".format(higherComputer))
        print("PLEASE TELL ME IF ITS HIGHER OR LOWER")
        higherComputer = computer
        counter += 1

    if player_value == "lower":
        lowerComputer = random.randint(0, computer)
        print("I AM GUESSING IT IS {}".format(lowerComputer))
        print("PLEASE TELL ME IF ITS HIGHER OR LOWER")
        lowerComputer = computer
        counter += 1

    if player_value == "correct":
        print("I HAVE GUESSED IT RIGHT AFTER {} TRIES".format(counter))


# def userinput():
#     print("please enter your number from 1-20")
#     user_input = int(input())
#     if user_input > 20:
#         print("please enter a number below 20")
#     if user_input < 0:
#         print("come on its not that hard")
#     return userinput()

while True:
    computerguess()
