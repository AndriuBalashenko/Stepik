def pig_it(text):
    return ' '.join([chars[1:] + chars[:1] + 'ay' if chars.isalpha() else chars for chars in text.split()])