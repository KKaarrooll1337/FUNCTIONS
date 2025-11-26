def nPrime(x):
    found_prime = 0
    num = 2
    
    while True:
        is_prime = True
        
        #czy dzieli się przez cokolwiek (od 2 w górę)
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime: #jeżeli jest pierwsza to odkładamy która to z kolei
            found_prime += 1
        
        if found_prime == x:
            return num
            
        num += 1