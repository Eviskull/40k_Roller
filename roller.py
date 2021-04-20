import random   # Used for dice rolls
import sys # parse CL arguments
"""
Updated from the original version at https://github.com/PearsHaveLand/40k_Roller
Now includes ability to roll ? sided dice a silly number of times

Still to give the random generator better randomness
"""
def roll_d6(sides=5):
    """Original writer implemented this for readability, I like it.
"""
    return random.randint(0,sides)

def get_dinput(ret_type=1):
    """Handles inputs and adjusts return for list index.
"""
    data = {1:'number', 2:'sides'}
    choice = int(input(f"Enter {data[ret_type]} of dice: "))
    if ret_type == 1:
        return choice
    elif ret_type ==2:
        return choice-1

def roll_dice(num, dsides=5):
    """ Each index holds the number of dice with each value.
     E.g. 0 -> 1s, 1 -> 2s, etc.
"""
    rolls = [0 for x in range(0, dsides+1)]
    for i in range(num):
        rolls[roll_d6(sides=dsides)] += 1
    return rolls
        
def display_rolls(roll_list, num_dice):
    """Refactored this to one line and added functionality, now shows
    {D6 Side} s|+ -- {rolls}/{uprolls} = {% of total rolls to 2 decimal places}
"""
    print("-------RESULTS-------")
    for entry in range(0, len(roll_list)):
        if roll_list[entry] == 0:
            pass # This ignores unrolled numbers to keep display clear
        else:
            print(f"{entry+1}s|+ -- {roll_list[entry]}|{sum(roll_list[entry:])} = {(roll_list[entry]/num_dice)*100:2.2f}%")
            
def roll_work(dxrolls, faces=5):
    """Part of tidying up menu_loop()
"""
    try:
        roll_dx = roll_dice(dxrolls, faces)
        display_rolls(roll_dx, dxrolls)
    except Exception as e:
        print(str(e))

def menu_loop():
    while True:
        print('\n---Rolling Tool---\nEnter 1 to roll D6\nEnter 2 to roll D?\nEnter Q to exit\n')
        user_choice = input('Enter your selection: ')
        if user_choice == '1':
            roll_work(get_dinput(1))
        elif user_choice == '2':
            roll_work(get_dinput(1), get_dinput(2))
        elif user_choice.upper() == 'Q':
            print('Quitting program')
            break
        else:
            print(f'No idea what happened but {user_choice} was what was picked\nso I\'m going to the menu.')
            pass
        

if __name__ == '__main__':
    if len(sys.argv) == 2:
        roll_work(int(sys.argv[1]))
    elif len(sys.argv) == 3:
        roll_work(int(sys.argv[1]), int(sys.argv[2])-1)
    else:
        menu_loop()
