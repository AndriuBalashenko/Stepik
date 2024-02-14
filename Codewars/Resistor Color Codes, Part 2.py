def encode_resistor_colors(ohms_string):
    """"""
    color = {0: 'black', 1: 'brown', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green', 6: 'blue',
             7: 'violet', 8: 'gray', 9: 'white'}

    num = ohms_string.replace(' ohms', '')
    res = list()

    if num[-1] == 'k':
        num = num.replace('k', '')
        num = float(num)
        if 0 < num < 10:
            res.append(color[int((num * 10) // 10)])
            res.append(color[int((num * 10) % 10)])
            res.append(color[2])
        elif num == 10:
            res.append(color[1])
            res.append(color[0])
            res.append(color[3])

        elif num == 100:
            res.append(color[1])
            res.append(color[0])
            res.append(color[4])

        elif 10 < num < 100:
            res.append(color[int(num // 10)])
            res.append(color[int(num % 10)])
            res.append(color[3])

        elif 100 < num < 1000:
            res.append(color[int(num // 100)])
            res.append(color[int(num % 100) // 10])
            res.append(color[4])

    elif num[-1] == 'M':
        num = num.replace('M', '')
        num = float(num)
        if 0 < num < 10:
            res.append(color[int((num * 10) // 10)])
            res.append(color[int((num * 10) % 10)])
            res.append(color[5])

        elif 10 < num < 100:
            res.append(color[int(num // 10)])
            res.append(color[int(num % 10)])
            res.append(color[6])

        elif 100 < num < 1000:
            res.append(color[int(num // 100)])
            res.append(color[int(num % 100) // 10])
            res.append(color[7])
    else:
        num = float(num)
        if 10 < num < 100:
            res.append(color[int(num // 10)])
            res.append(color[int(num % 10)])
            res.append(color[0])

        elif num == 100:
            res.append(color[1])
            res.append(color[0])
            res.append(color[1])

        elif 100 < num < 1000:
            res.append(color[int(num // 100)])
            res.append(color[int(num % 100 // 10)])
            res.append(color[1])

        else:
            res.append(color[1])
            res.append(color[0])
            res.append(color[0])

    return ' '.join(res) + ' gold'

