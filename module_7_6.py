def mask_pin(n):
    masked_n = ""  
    
    for i in range(len(n)):
        if i in range(2, 12):
            masked_n += "*"
        else:
            masked_n += n[i]
            
    return masked_n