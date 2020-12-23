def solution(A):

    Total = 0
    Min = 100000
    P1 = 0
    for a in A:
        Total = Total + a
    for i in range(len(A)):
        P1 = P1+ A[i]
        P2 = Total-P1
        Diff = abs(P2 - P1)
        if Diff == 0:
            Min = 0
            return Min
        if Diff < Min:
            Min = Diff
           

    return Min 
    
    #Task Score 84%   Correctness 71%  Performance 100%
