def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
  
    list = [0] * n
    
    list[0] = 0
    list[1] = 1
    
    for i in range(2, n):
        list[i] = list[i-1] + list[i-2]
        
    return list[n-1]