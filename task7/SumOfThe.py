def SumOfThe(N, data):
    
    for i in range (N):
    
        total = 0
    
        for j in range (N):
        
            if j != i:
            
                total += data[j]
        
        if  total == data[i]:
        
            return total
