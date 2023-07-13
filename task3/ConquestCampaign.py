def ConquestCampaign(N, M, L, battalion):
    map = []
    for i in range (N):
        row = []
        for j in range (M):
            row.append(0)
        map.append(row)
    
    for i in range (int(len(battalion)/2)):
        map[battalion[i*2]-1][battalion[i*2+1]-1] = 1
        
    count = 1
    hasZeroes =  True
    
    while hasZeroes:
        
        hasZeroes = False
        for i in range (N):
            for j in range (M):
                if map[i][j] == 0:
                    hasZeroes = True
                    count += 1
                    break
            if hasZeroes:
                break

        for i in range (N):
            for j in range (M):
                if map[i][j] != 0:
                    map[i][j] += 1

        for i in range (N):
            for j in range (M):
                if map[i][j] == 0:
                    if i > 0 and map[i-1][j] == 2:
                        map[i][j] = 1
                    elif j > 0 and map[i][j-1] == 2:
                        map[i][j] = 1
                    elif i < N-1 and map[i+1][j] == 2:
                        map[i][j] = 1
                    elif j < M-1 and map[i][j+1] == 2:
                        map[i][j] = 1

    return count
