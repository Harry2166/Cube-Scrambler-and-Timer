# Cube-Scrambler-and-Timer
A Rubik's Cube scrambler and timer made in Python.

This is the first project by Harry2166.

For those without experience in using or solving a Rubik's Cube, refer to the following link:
https://ruwix.com/the-rubiks-cube/notation/

This code has three functions:
- To give a scramble for the Rubik's Cube
- To have a timer for the Rubik's Cube
- To store the times in a separate .txt file

In order to scramble of the cube, there were three lists that contains the three different types of rotation or moves (as specified in the code), the clockwise, counterclockwise, and double turn.

There is a random number generator that was used in order to determine which type of rotation would be used, with each type of rotation being assigned with a certain number from 1 to 3.

From then, based on the number, the random.choice() function would be used in order to pick the move to be added for the scramble. In order to make sure that moves are not doubled or cancelled, the index of the previous element of the list in the scramble would be compared to the current index of the generated elemenet. If they were equivalent to each other, a while loop will be used to randomize the values until their indices would be different.

*This is my first project that I've done and posted here in GitHub, it isn't the best and I know it can be improved but it's worth posting here!*
