def number_pattern (n):
    if not isinstance(n,int):
        return ("Argument must be an integer value.")
    if n < 1:
        return ("Argument must be an integer greater than 0.")
    s = ""
    for i in range (1,n+1):
        if i == n:
            s += str(i)
        else:
            s += str(i) +" "
    return (s)    
print (number_pattern(4))
print (number_pattern(12))