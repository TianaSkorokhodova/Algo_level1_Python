def squirrel(N):
    
    factorial = 1
    for i in range(2, N+1):
        factorial *= i
        
    factorial_string = str(factorial)
    
    return int(factorial_string[0])
