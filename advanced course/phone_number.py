"""
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.
"""


def create_phone_number(n: list) -> str:
    return f'({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}'


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

v = create_phone_number([0,2,9,5,7,4,1,2,0,5])
print(v)