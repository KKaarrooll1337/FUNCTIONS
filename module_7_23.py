def checkPassword(x):
    if len(x) < 6:
        return print("Password too short!")
    else:
        for char in x:
            if x.count(char) > 1:
                return print("Spotted repeated sign!")
    
    return print("Alrighty buddy")