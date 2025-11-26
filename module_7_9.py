def num_sum(n, bl):

    suma = 0
    str_n = str(n)
    
    for char in str_n:
        char_int = int(char)
        
        if bl:
            if char_int  % 2 == 0:
                suma += char_int 
        else:
            if char_int  % 2 != 0:
                suma += char_int 
                
    return suma