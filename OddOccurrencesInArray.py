def solution(A):
    A.sort()

    def delDouble(A):
        if len(A) == 1 :
            return A[0]

        if A[-1] == A[-2]:
            del A[-1]
            del A[-1]
            delDouble(A)
        else:
            return A[-1]

 
    delDouble(A)
 
    return   A[-1]
    
    
    #task score 66% , correctness 100%, performance 25%
