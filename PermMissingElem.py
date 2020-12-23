def solution(A):
    L= len(A)
    T = int((1+L)*L/2)
    # print("total")
    # print(T)
    F = 0
    for i in A:
        F = F + i
    dist = F-T  
    # print("distance")
    # print(dist)
    res = L+1-dist 
    # print("result")
    # print(res) 
    return res
    
    # must consider A begin with 1
