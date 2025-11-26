def f(x):
    #pierwsza cyfra jako wynik startowy
    result = int(x[0])
    
    # naprzemian są cyfry i operatory więc pętla skacze co 2
    for i in range(1, len(x), 2):
        operator = x[i]
        number = int(x[i+1])
        
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
            
    return result