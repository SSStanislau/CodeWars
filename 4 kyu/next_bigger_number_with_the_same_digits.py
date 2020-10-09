'''
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
'''


def next_bigger(n):
    s = str(n)
    for i in range(len(s)-1,0,-1):
        h = s[:i-1]
        if(s[i] > s[i-1]): 
            arr = list(s[i:])
            t = sorted([x for x in arr if x > s[i-1]])[0]
            arr.remove(t)
            arr.append(s[i-1])
            arr.sort()
            return int(h + t + ''.join(arr))
    return -1