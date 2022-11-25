"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil

"""
def next_bigger(n):
    s = str(n)
    if check(s):
        return -1
    l = len(s)
    ss = []
    for item in s:
        ss.append(int(item))
    index = l-1
    while(index > 0):
        if int(ss[index-1]) < int(ss[index]):
            for j in range(l-1,index-1,-1):
                if ss[j] > ss[index-1]:
                    temp = ss[j]
                    ss[j] = ss[index-1]
                    ss[index-1] = temp
                    ss = ss[:index] + ss[index:][::-1]
                    break
            break
        else:
            index -=1
    res = 0
    for i in range(0,l):
        res += 10 ** i * ss[-(i+1)]
    return res
def check(s):
    l = len(s)
    index = l-1
    while(index > 0):
      if int(s[index]) >  int(s[index-1]):
          return False
      index -=1
    return True

next_bigger(5)