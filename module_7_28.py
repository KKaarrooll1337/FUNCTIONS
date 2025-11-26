def max_streak(x):
    max_streak = 0
    digit_with_max_streak = 0
    current_streak = 0
    current_digit = x[0]
    
    for char in x:
        if char == current_digit:
            current_streak += 1
        else:
            if current_streak > max_streak:
                max_streak = current_streak
                digit_with_max_streak = int(current_digit)
            
            current_digit = char
            current_streak = 1
        
    return digit_with_max_streak