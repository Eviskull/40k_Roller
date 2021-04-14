import random   # Used for dice rolls
# import sys
"""
 Returns a random number between 0 and 5, inclusive. It's not 1 to 6 because I
 only care about how many of each number are rolled. So these just generate the
 indices of a list, rather than the actual dice value
 Added this function for readability. Plus, typing roll_d6 is just easier than
 random.randint
 
 Refactored after finding it on github and needing to read some code I didn't write to make sense of it.
"""
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
    
    
def display_rolls(roll_list, num_dice):
    #Refactored this to one line and added functionality, now shows
    #{D6 Side} s|+ -- {rolls}/{uprolls} = {% of total rolls to 2 decimal places}
    for entry in range(0, len(roll_list)):
        print(f"{entry+1}s|+ -- {roll_list[entry]}|{sum(roll_list[0:entry+1])} = {(roll_list[entry]/num_dice)*100:2.2f}%")
        
def get_rollnumber():
    #Break up inputs for debugging
    return int(input('Enter number of dice to throw?'))


def main_loop():
    while True:
        print('\nHello and welcome to the rolling tool\nEnter 1 to roll\nEnter Q to exit\n')
        user_choice = input('Enter your selection: ')
        if user_choice == '1':
            print(user_choice, '1')
            try:
                d6rolls = get_rollnumber()
                display_rolls(roll_dice(d6rolls), d6rolls)
            except Exception as e:
                print(str(e))
        elif user_choice.upper() == 'Q':
            print('Quitting program')
            break
        else:
            print(f'No idea what happened but {user_choice} was what was picked\nso I\'m quitting to be safe.')
            break
        


if __name__ == '__main__':
    main_loop()
