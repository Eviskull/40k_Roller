import random
import sys


def roll_d6():
    return random.randint(0,5)

def roll_dice(num):
    rolls = [0, 0, 0, 0, 0, 0]
    for i in range(num):
        rolls[roll_d6()] += 1
    return rolls

def display_rolls(roll_list):
    print("6+ -- ", roll_list[5])
    print("5+ -- ", roll_list[5] + roll_list[4])
    print("4+ -- ", roll_list[5] + roll_list[4] + roll_list[3])
    print("3+ -- ", roll_list[5] + roll_list[4] + roll_list[3] + roll_list[2])
    print("2+ -- ", roll_list[5] + roll_list[4] + roll_list[3] + roll_list[2] + roll_list[1])
    print("1+ -- ", roll_list[5] + roll_list[4] + roll_list[3] + roll_list[2] + roll_list[1] + roll_list[0])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid syntax, please enter:\n'roller.py <number of dice to roll>'")
        sys.exit()
    num_dice = int(sys.argv[1])
    display_rolls(roll_dice(num_dice))
