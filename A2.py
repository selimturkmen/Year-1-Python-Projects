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
    pos = 0
    if x <= 5:  # Fast Plod - 50% (ie. 1-5), 3 squares forward
        pos += 3
    elif 7 >= x >= 6:  # Slip - 20% (ie. 6-7), 6 squares back
        pos -= 6
    else:  # Slow Plod - 30% (ie. 8-10), 1 square forward
        pos += 1

    return pos


def hare_move(x):
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

    t_pos = 1
    h_pos = 1
    while t_pos < 70 or h_pos < 70:

        x = random.randint(1,10)
        y = random.randint(1,10)

        t_pos += tortoise_move(x)
        #print(t_pos)
        h_pos += hare_move(y)
        #print(h_pos)

        if abs(t_pos) == t_pos and abs(h_pos) == h_pos:
            if t_pos == h_pos:
                for i in range(t_pos - 1):
                    print(" ", end="")
                print("OUCH!!!",end="")
            if t_pos > h_pos:
                f = t_pos
                s = h_pos
                t = f - s

                for k in range(s - 1):
                    print(" ",end="")
                print("H",end="")
                for j in range(t - 1):
                    print(" ",end="")
                print("T",end="")
            if t_pos < h_pos:
                s = h_pos
                f = t_pos
                t = s - f

                for k in range(f - 1):
                    print(" ",end="")
                print("T",end="")
                for j in range(t - 1):
                    print(" ",end="")
                print("H",end="")

        elif abs(t_pos) != t_pos and abs(h_pos) != h_pos:
            t_pos = 1
            h_pos = 1
            print("OUCH!!!",end="")

        elif abs(t_pos) != t_pos:
            t_pos = 1
            if t_pos == h_pos:
                for i in range(t_pos - 1):
                    print(" ", end="")
                print("OUCH!!!",end="")
            if t_pos < h_pos:
                s = h_pos
                f = s - t_pos
                t = s - f

                for k in range(t - 1):
                    print(" ",end="")
                print("T",end="")
                for j in range(f - 1):
                    print(" ",end="")
                print("H",end="")

        elif abs(h_pos) != h_pos:
            h_pos = 1
            if t_pos == h_pos:
                for i in range(t_pos - 1):
                    print(" ", end="")
                print("OUCH!!!",end="")

            if t_pos > h_pos:
                f = t_pos
                s = f - h_pos
                t = f - s

                for k in range(t - 1):
                    print(" ",end="")
                print("H",end="")
                for j in range(s - 1):
                    print(" ",end="")
                print("T",end="")


        print(" ")


    print("Tortoise final position {}".format(t_pos))
    print("Hare final position {}".format(h_pos))

    if t_pos > h_pos:
        print("TORTOISE WIN!!! YAY!!!")
    elif t_pos < h_pos:
        print("Hare wins.")
    else:
        print("It's a tie.")


if __name__ == '__main__':
    main()
