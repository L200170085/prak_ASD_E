a = [[1,2], [1,2]]
b = [[5, 6],[8, 9,]]
def cekKonsisten(n) :
    x = len(n[0])
    z = 0
    for i in range (len(n)) :
        if (len(n[i]) == x) :
            z += 1
    if (z == len(n)) :
        print ("Matriks konsisten")
    else :
        print ("Matriks tidak konsisten")

cekKonsisten(a)
cekKonsisten(b)

def cekIsi(n) :
    x = 0
    y = 0
    for i in n :
        for j in i :
            y += 1
            if (str(j).isdigit() == False) :
                print ("tidak semua isi matriks adalah angka")
                break
            else :
                x += 1
    if (x == y):
        print ("semua isi matriks adalah angka")

cekIsi(a)
cekIsi(b)

def ordo(n) :
    x, y = 0, 0
    for i in range (len(n)) :
        x += 1
        y = len(n[i])
    print ("mempunyai ordo "+str(x)+"x"+str(y))

ordo(a)


def menjumlahkan(n,m):
    x, y =0, 0

    for i in range (len(n)):
        x += 1
        y = len(n[i])
    xy = [[0 for j in range(x)] for i in range (y)]

    z = 0
    if(len(n) == len(m)):
        for i in range(len(n)):
            if(len(n[i]) == len(m[i])):
                z += 1
    if(z==len(n) and z==len(m)):
        print ("mempunyai ukuran sama")
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j] = n[i][j] + m[i][j]
        print (xy)
    else :
        print ("ukuran beda")

menjumlahkan(a,b)

def mengkalikan(n,m):
    x, y = 0, 0
    for i in range(len(n)):
        x += 1
        y = len(n[i])
    v,w = 0, 0
    for i in range(len(n)):
        v += 1
        y = len(n[i])

    if (y==v):
        print ("bisa dikalikan")
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    vwxy[i][j] += n[i][k] * m[k][j]
        print (vwxy)
    else :
        print ("tidak memenuhi syarat")

zz = [[1,2,3], [1,2,3]]
zx = [[1],[2],[3]]
mengkalikan(zz, zx)

def determHitung(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determHitung(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    else:
        return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    return total

z = [[3,1], [2,5]]
print (determHitung(z))
