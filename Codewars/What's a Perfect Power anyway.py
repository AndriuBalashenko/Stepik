def isPP(n):
    r = list()
    for i in range(1, n // 2 + 1):
        for j in range(1, n // 2 + 1):
            k = i ** j
            if i ** j == n:
                r.append(i)
                r.append(j)
                return r
            elif i ** j > n:
                break
    return None

print(isPP(4))