import math
def solution(X, Y, D):
    Dist = Y - X
    A = math.ceil(Dist/D)
    # print(A)
    return A
