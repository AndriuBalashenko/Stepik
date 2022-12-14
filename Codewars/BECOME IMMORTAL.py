"""
In the nation of CodeWars, there lives an Elder who has lived for a long time. Some people call him the Grandpatriarch,
 but most people just refer to him as the Elder.

There is a secret to his longetivity: he has a lot of young worshippers, who regularly perform a ritual to ensure that
the Elder stays immortal:

The worshippers line up in a magic rectangle, of dimensions m and n.
They channel their will to wish for the Elder. In this magic rectangle, any worshipper can donate time equal to the xor
of the column and the row (zero-indexed) he's on, in seconds, to the Elder.
However, not every ritual goes perfectly. The donation of time from the worshippers to the Elder will experience a
transmission loss l (in seconds). Also, if a specific worshipper cannot channel more than l seconds, the Elder will not
 be able to receive this worshipper's donation.
The estimated age of the Elder is so old it's probably bigger than the total number of atoms in the universe. However,
the lazy programmers (who made a big news by inventing the Y2K bug and other related things) apparently didn't think
thoroughly enough about this, and so their simple date-time system can only record time from 0 to t-1 seconds. If the
elder received the total amount of time (in seconds) more than the system can store, it will be wrapped around so that
the time would be between the range 0 to t-1.

Given m, n, l and t, please find the number of seconds the Elder has received, represented in the poor programmer's
date-time system.

(Note: t will never be bigger than 2^32 - 1, and in JS, 2^26 - 1.)
"""


def larger_pow(x):
    t = 1
    while t < x:
        t <<= 1
    return t


def range_sum(l, r):
    return (l + r) * (r - l + 1) // 2


def elder_age(m, n, l, t):
    if m == 0 or n == 0:
        return 0
    if m > n:
        m, n = n, m
    lm, ln = larger_pow(m), larger_pow(n)
    if l > ln:
        return 0

    if lm == ln:
        return (range_sum(1, ln - l - 1) * (m + n - ln) + elder_age(ln - n, lm - m, l, t)) % t

    if lm < ln:
        lm = ln // 2
        tmp = range_sum(1, ln - l - 1) * m - (ln - n) * range_sum(max(0, lm - l), ln - l - 1)
        if l <= lm:
            tmp += (lm - l) * (lm - m) * (ln - n) + elder_age(lm - m, ln - n, 0, t)
        else:
            tmp += elder_age(lm - m, ln - n, l - lm, t)
        return tmp % t