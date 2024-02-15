# def first_non_repeating_letter(s):
#     for c in s:
#         if s.find(c.lower()) == s.rfind(c.lower()):
#             return c
#     return ''


def first_non_repeating_letter(s):
    res = [c for c in s if s.lower().count(c.lower()) == 1]
    r = None
    if len(res) > 0:
        r = res[0]
    return r


print(first_non_repeating_letter(""))
