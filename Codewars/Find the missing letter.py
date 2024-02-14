def find_missing_letter(chars):
    'find missing letter'
    for i in range(ord(chars[0]), ord(chars[-1]) + 1):
        if chr(i) not in chars:
            return chr(i)