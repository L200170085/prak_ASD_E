def gabungUrut(A, B):
    c = []
    tIdxA = len(A)
    tIdxB = len(B)
    a = 0
    b = 0

    while len(c) != tIdxA + tIdxB :
        if a < tIdxA-1 and A[a] < B[b]:
            c.append(A[a])
            a += 1
        elif b < tIdxB-1 and B[b] < A[a]:
            c.append(B[b])
            b += 1
        else :
            c.append(A[a])
            c.append(B[b])
            a += 1
            b += 1
        if a == tIdxA:
            c = c+B[b:]
        elif b == tIdxB:
            c = c+A[a:]
    return c

jk = [1,2,4,5,7,8,9]
jl = [3,10,11,12,16,14]
j = gabungUrut(jk, jl)
print (j)
