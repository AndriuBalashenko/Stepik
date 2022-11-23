"""
For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter. For example, the
input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or
None -- see sample tests.
"""

def first_non_repeating_letter(string):
    reps = [c for c in string if string.lower().count(c.lower()) == 1]
    return  reps[0] if len(reps) > 0 else ""