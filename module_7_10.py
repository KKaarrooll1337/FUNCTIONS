def countNum(x, y):
    count = 0
    # Poprawka zakresu: idziemy od x do y (y+1 żeby uwzględnić y)
    for i in range(x, y + 1):
        # Sprawdzamy tylko liczby ujemne mniejsze od -1 (-1 nie jest pierwsze)
        if i < -1:
            j = i
            abs_j = abs(j)
            abs_i = abs(i)
            
            # WAŻNE: Resetujemy flagę xd dla każdej liczby z osobna!
            xd = True 
            
            # Twoja pętla sprawdzająca dzielniki "od tyłu"
            # Używamy innej nazwy zmiennej iteracyjnej (k), żeby nie myliła się z abs_j
            for k in range(abs_j, 2, -1):
                # Twój warunek:
                if abs_i % (k - 1) == 0:
                    xd = False
                    break
            
            if xd == True:
                count += 1
                
    return count