def solution(A):

    freq = {} 
    for num in A: 
        if (num in freq): 
            freq[num] += 1
        else: 
            freq[num] = 1
    
    for key, value in freq.items():
        if value % 2 == 1:
            return key
 #task score 100% , correctness 100%, performance 100%


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
    #conclusion: operate the list,such as del list[i] is not a good idea.
