def solve(A):
    sort_list = []
    
    for i in range(len(A)):
        A[i] = (A[i]**2)
    
    start = 0
    end = -1
    while len(A) != len(sort_list):
        if A[start] >= A[end]:
            sort_list.append(A[start])
            start += 1
        else:
            sort_list.append(A[end])
            end -= 1
    sort_list.reverse()
    return sort_list