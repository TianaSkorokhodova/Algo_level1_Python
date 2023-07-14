def SynchronizingTables(N, ids, salary):
    
    ids_sort = sorted(ids)
    salary_sort = sorted(salary)
    
    salary_sort_new = []
    
    for i in range (N):
    
        salary_sort_new.append(salary_sort[ids_sort.index(ids[i])])
    
    return salary_sort_new
