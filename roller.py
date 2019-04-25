import random   # Used for dice rolls
import sys      # Used for parsing command line arguments

# Returns a random number between 0 and 5, inclusive. It's not 1 to 6 because I
# only care about how many of each number are rolled. So these just generate the
# indices of a list, rather than the actual dice value
# Added this function for readability. Plus, typing roll_d6 is just easier than
# random.randint
def roll_d6():
    return random.randint(0,5)

def roll_dice(num):

    # Each index holds the number of dice with each value.
    # E.g. 0 -> 1s, 1 -> 2s, etc.
    rolls = [0, 0, 0, 0, 0, 0]

    # Rolls the specified number of dice, adding 1 to a random index each time
    for i in range(num):
        rolls[roll_d6()] += 1
    return rolls

# It was late and I was tired when I wrote this, so I hard-coded it all instead
# of doing a nifty for loop or something.
def display_rolls(roll_list):
    print("6+ -- ", roll_list[5])
    print("5+ -- ", roll_list[5] + roll_list[4])
    print("4+ -- ", roll_list[5] + roll_list[4] + roll_list[3])
    print("3+ -- ", roll_list[5] + roll_list[4] + roll_list[3] + roll_list[2])
    print("2+ -- ", roll_list[5] + roll_list[4] + roll_list[3] + roll_list[2] + roll_list[1])
    print("1+ -- ", roll_list[5] + roll_list[4] + roll_list[3] + roll_list[2] + roll_list[1] + roll_list[0])

if __name__ == "__main__":

    # Check for command line args
    if len(sys.argv) != 2:
        print("Invalid syntax, please enter:\n'roller.py <number of dice to roll>'")
        sys.exit()

    # Grab the number of dice from the provided arg
    num_dice = int(sys.argv[1])

    # Roll dice then print the results
    display_rolls(roll_dice(num_dice))
