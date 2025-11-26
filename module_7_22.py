def getAcronym(x):
    result = ""
    flag = 1
    for char in x:
        if flag == 1:
            result += char
            flag = 0
        if char == " ":
            flag = 1
    
    return result