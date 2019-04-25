# 40k Dice Roller

## Purpose
Warhammer 40,000 can be a slow game, especially players need to roll more dice than they can carry. This Python program helps make casual Warhammer 40,000 flow a little faster. When 50+ dice need to be rolled at once, it's nice to resolve an attack quickly with this dice roller.

I recommend using this only when the number of attacks to be rolled exceeds the number of dice that can reasonably fit in your hand. My limit is about 35.

## How it Works
Just run `python3 <number_of_dice>` and press enter. Output is formatted for 40k specifically, so it mainly specifies "ups," meaning how many dice reached or exceeded a given number. For example, output of `5+ -- 10` means that 10 dice rolled "5-ups," i.e. 10 dice with at least a value of 5.

## Future Plans
I'm going to implement an interactive mode, so you can just enter the number of dice to be rolled, rather than running python3 every time you want to use this utility.

Also, using a better pseudorandom function might be a good idea. Python's random isn't useful for cryptographic security, and we all know 40k is more important than cryptography.
