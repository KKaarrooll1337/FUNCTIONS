def isPalindrome(x):
    i = 0
    h = 0
    e = 0
    list =  [""] * len(x)
    for char in x:
        list[e] = char
        e +=1
    for i in range(len(x)//2):
        q = len(x) - 1
        if list[i] != list[q-h]:
            return False
        h += 1
    return True