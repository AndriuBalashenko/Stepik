"""
Complete the greatestProduct method so that it'll find the greatest product of five consecutive
digits in the given string of digits.

For example:

greatestProduct("123834539327238239583") // should return 3240
The input string always has more than five digits.

Adapted from Project Euler.
"""

def greatest_product(n):
    mx = 0
    for i in range(len(n)+1):
        pr = 1
        for x in n[i:i+5]:
            if len(n[i:i+5]) < 5 or "0" in n[i:i+5]:
                break
            pr = pr * int(x)
        if pr > mx and pr != 1: mx = pr
    return mx