def LineAnalysis (line) :
    pointCounter = 0
    prevPoint = -1
    result = True

    for i in range (1, len(line)) :   

        if line[i] == "." :
            pointCounter += 1
        if line[i] == "*" :

            if prevPoint != -1 and prevPoint != pointCounter :
                result = False
                break
            prevPoint = pointCounter
            pointCounter = 0

    return result    
