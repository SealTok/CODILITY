def solution(A):
    # A = [-1000,1000]
    s = 0
    p = 0
    t = 0
    m=2000
    for a in A:
        s+=a
    for i in range(len(A)-1):
        p+=A[i]
        t = abs(s-p-p)
        # print t
        if t<m:
            m = t
    return m

 #Task Score 100%   Correctness 100%  Performance 100%
    
    
    
def solution(A):

    Total = 0    // s
    Min = 100000  //m
    P1 = 0        //p
    for a in A:
        Total = Total + a
    for i in range(len(A)):    //mistake!!
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
