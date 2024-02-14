def unique_in_order(sequence):
    string = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i - 1]:
            string.append(sequence[i])
    return string