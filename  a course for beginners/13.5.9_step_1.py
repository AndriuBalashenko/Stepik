# def simple_numbers(n):
#     n = int(n)
#     count = 0
#     for i in range(2, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 1:
#         return True
#     else:
#         return False
#
# num = input()
#
# print(simple_numbers(num))

def if_palindrome(a):
    return (str(a) == str(a)[::-1])

num = input()
print(if_palindrome(num))

