def solution(X, A):
    B = [0]*X
    total = 0

 
    for i in range(len(A)):
        a = A[i]-1
        if  B[a] != 1 :
            B[a] = 1
            total += 1
        if total == X:       #  cannot do it only after the above row. 
            return i
        
    return  -1
  # Task 100%  Correct 100%  Performance 100%  


def solution(X, A):
    river = [0 ]*(X+1)
    river[0] = 1
    total = 1

    for i, num in enumerate(A):
        if river[num] == 1:
            continue                         # not to use  is OK
        elif river[num] == 0:
            river[num] = 1
            total += 1                       #set total, to improve

        if total == X+1:
            return i

    return -1
  
  
#Task 100%  Correct 100%  Performance 100%  


def solution(X, A) :
   B = [0]* X
    Target = int((1+X)*X/2)      #too complex
    TotalB = 0
    res = 0
    for i in range(len(A)):
        a = A[i]
        if a <= X:
            B[a-1] = a
            if i >= X-1:
                TotalB = sum(B)
                # print(TotalB) 
                # print(Target)
                if TotalB == Target:
                   res = i
                   return res
            if i == len(A)-1:
                res = -1
    return  res

#Task 63%  Correct 100%  Performance 20%
  
  ///////////////////////////
def solution(X, A) :
  temp = []
  for i in range(0, len(A)) :
    if(A[i]<=X) :
      temp.append(A[i])     
      if( len(set(temp)) == X) :
        return i
  if (len(set(temp))!=X) :
    return -1 
    Task54%  Correct100% Performance 0%
    
    
    
    
    
    
