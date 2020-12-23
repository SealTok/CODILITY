def solution(A, K):
    if K == 0 or len(A) == 0:
        # print(A)
        return A
    if K > 0:
        O = A
        # print(O)
        for i in range(K):
            L = A[-1]
            del A[-1]
            # print(L)
            # print(A)
            A.insert(0,L)
            # print(A)
            i = i + 1
            if i == K:
                # print(A)
                return A
