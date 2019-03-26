from time import time as detak
from random import shuffle as kocok

def swap(a, b, c):
    a[b], a[c] = a[c], a[b]

def cariPosisiYangTerkecil(a, darisini, sampaisini):
    posisiTerkecil = darisini
    for i in range(darisini+1, sampaisini):
        if a[i] < a[posisiTerkecil]:
            posisiTerkecil = i
    return posisiTerkecil

def bubleSort(A):
    a = len(A)
    for i in range(a-1):
        for j in range(a-i-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

k = [i for i in range(1, 6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubleSort(u_bub);ak=detak();print('Bubble : %g detik' %(ak - aw));
aw = detak();selectionSort(u_sel);ak=detak();print('Selection : %g detik' %(ak - aw));
aw = detak();insertionSort(u_ins);ak=detak();print('Insertion : %g detik' %(ak - aw));

"""
hasil dari running didapat :
Bubble : 16.9799 detik
Selection : 5.45706 detik
Insertion : 6.81968 detik

terbukti bahwa Pengurutan data menggunakan Algoritma Bubble sort memakan waktu yang cukup lama, sehingga disarankan menggunakan Algoritma Selection atau Insertion. Walaupun masih ada Algoritma yang lain.
"""
