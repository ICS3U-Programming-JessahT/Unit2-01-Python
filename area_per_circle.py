#!/usr/bin/env python3

# Created By: Jessah
# Date: Sept 23, 2022
# This program calculates the area and circumference of a circle.

import math

rad = 6


def main():
    print("If a circle has a radius of 15mm")
    print("The circumference is:{}".format(2 * math.pi * rad))
    print("")
    print("The area is:{}".format(math.pi * rad**2))


if __name__ == "__main__":
    main()
