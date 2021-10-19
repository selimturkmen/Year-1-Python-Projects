"""This program re-creates the classic race of the tortoise and the hare
and uses random number generation to develop a simulation of this.
There are 70 squares and both the tortoise and the hare start square 1,
and through a random number generation, their movement will be decided.
Their movement can be good (moving up a number of squares) or harmful
(slipping down a number of squares). This will happen by generating
a random number from 1-10, and computing which movement will
take place depending on the number

Author: Selim Turkmen
Section: CISC 121 - 002
Student Number: 20260414
Date Submitted: 2021-10-19
"""

import random


def tortoise_move(x):
    # Initialize position variable (how much is added to t_pos)
    pos = 0
    if x <= 5:  # Fast Plod - 50% (ie. 1-5), 3 squares forward
        pos += 3
    elif 7 >= x >= 6:  # Slip - 20% (ie. 6-7), 6 squares back
        pos -= 6
    else:  # Slow Plod - 30% (ie. 8-10), 1 square forward
        pos += 1

    return pos


def hare_move(x):
    # Initialize position variable (how much is added to h_pos)
    pos = 0

    if x <= 2:  # Sleep - 20% (ie. 1-2), no movement
        pos = pos
    elif 4 >= x >= 3:  # Big Hop - 20% (ie. 3-4), 9 squares forward
        pos += 9
    elif x == 5:  # Big Slip - 10% (ie. 5), 12 squares back
        pos -= 12
    elif 8 >= x >= 6:  # Small Hop - 30% (ie. 6-8), 1 square up
        pos += 1
    else:  # Small Slip - 20% (ie. 9-10), 2 squares back
        pos -= 2

    return pos


def main():
    print("BANG!!!")
    print("AND THEY ARE OFF!!!")

    # Initialization of position variables for Tortoise and Hare.
    # Both start at square 1
    t_pos = 1
    h_pos = 1

    # While loop that runs until either animal reaches the end
    # Once one reaches square 70, loop stops running
    while t_pos < 70 and h_pos < 70:

        # x,y are random ints that are created at every iteration of the loop
        x = random.randint(1, 10)
        y = random.randint(1, 10)

        # Calls movement functions, with the random int to determine movement
        # Movement that is calculated is added to their current position
        t_pos += tortoise_move(x)
        h_pos += hare_move(y)

        # If either position goes to zero (by subtraction)
        # they are reset to 1 - no square 0
        if t_pos == 0:
            t_pos = 1
        if h_pos == 0:
            h_pos = 1

        # Possibility 1: Both position values are positive

        if abs(t_pos) == t_pos and abs(h_pos) == h_pos:

            # Check if they are tied
            if t_pos == h_pos:
                # Loop to print spaces for the position they are tied at,
                # followed by OUCH!!!
                for i in range(t_pos - 1):
                    print(" ", end="")
                print("OUCH!!!", end="")

            # Check if Tortoise is winning
            if t_pos > h_pos:
                # F: Tortoise position
                # S: Hare position
                # T: Difference between the two (for output)
                f = t_pos
                s = h_pos
                t = f - s

                # Loop to print Hare position with spaces and H
                # Because Hare is losing and farther behind
                for k in range(s - 1):
                    print(" ", end="")
                print("H", end="")
                # Loop to print Tortoise position with spaces and T, after H
                # Because Tortoise is winning and ahead
                for j in range(t - 1):
                    print(" ", end="")
                print("T", end="")

            # Check if Hare is winning
            if t_pos < h_pos:
                # S: Hare position
                # F: Tortoise position
                # T: Difference between the two (for output)
                s = h_pos
                f = t_pos
                t = s - f

                # Loop to print Tortoise position with spaces and T
                # Because Tortoise is losing and farther behind
                for k in range(f - 1):
                    print(" ", end="")
                print("T", end="")
                # Loop to print Hare position with spaces and H, after T
                # Because Hare is winning and ahead
                for j in range(t - 1):
                    print(" ", end="")
                print("H", end="")


        # Possibility 2: Both positions are negative (both slipped)

        elif abs(t_pos) != t_pos and abs(h_pos) != h_pos:
            # Put both positions to start and print OUCH!!! since they are tied
            t_pos = 1
            h_pos = 1
            print("OUCH!!!", end="")


        # Possibility 3: Tortoise slipped and is at negative position

        elif abs(t_pos) != t_pos:
            # Set Tortoise position to square 1
            t_pos = 1
            # If Hare is also at square 1, print OUCH!!!
            if t_pos == h_pos:
                for i in range(t_pos - 1):
                    print(" ", end="")
                print("OUCH!!!", end="")

            # Otherwise, Hare is ahead
            if t_pos < h_pos:
                # S: Hare position
                # F: Difference between Hare and Tortoise (always H_Pos - 1)
                # T: Hare - Difference
                s = h_pos
                f = s - t_pos
                t = s - f

                # Output Tortoise position first at 1
                for k in range(t - 1):
                    print(" ", end="")
                print("T", end="")
                # Output Hare position at T
                for j in range(f - 1):
                    print(" ", end="")
                print("H", end="")


        # Possibility 4: Hare slipped and is at a negative position

        elif abs(h_pos) != h_pos:
            # Set Hare position to square 1
            h_pos = 1
            # If Tortoise is also at square 1, print OUCH!!!
            if t_pos == h_pos:
                for i in range(t_pos - 1):
                    print(" ", end="")
                print("OUCH!!!", end="")

            # Otherwise, Tortoise is ahead
            if t_pos > h_pos:
                # F: Tortoise position
                # S: Difference between Tortoise and Hare (always t_pos - 1)
                # T: Tortoise - Difference
                f = t_pos
                s = f - h_pos
                t = f - s

                # Output Hare position at square 1
                for k in range(t - 1):
                    print(" ", end="")
                print("H", end="")
                # Output Tortoise position at S
                for j in range(s - 1):
                    print(" ", end="")
                print("T", end="")

        # Print new line
        print(" ")

    # Print both animals final position once While loop stopped running
    print("Tortoise final position {}".format(t_pos))
    print("Hare final position {}".format(h_pos))

    # Check all three possibilities of race outcome and print response
    if t_pos > h_pos:
        print("TORTOISE WIN!!! YAY!!!")
    elif t_pos < h_pos:
        print("Hare wins.")
    else:
        print("It's a tie.")


if __name__ == '__main__':
    main()
