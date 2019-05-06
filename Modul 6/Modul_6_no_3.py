from time import time as detak
from random import shuffle as kocok


def mergeSort(a):
	# print ("membelah", a)
	if len(a) > 1 :
		mid = len(a) // 2
		separuhKiri = a[:mid]
		separuhKanan = a[mid:]

		mergeSort(separuhKiri)
		mergeSort(separuhKanan)

		i = 0
		j = 0
		k = 0

		while i < len(separuhKiri) and j < len(separuhKanan) :
			if separuhKiri[i] < separuhKanan[j] :
				a[k] = separuhKiri[i]
				i = i + 1
			else :
				a[k] = separuhKanan[j]
				j = j + 1
			k = k + 1

		while i < len(separuhKiri) :
			a[k] = separuhKiri[i]
			i = i + 1
			k = k + 1

		while j < len(separuhKanan) :
			a[k] = separuhKanan[j]
			j = j + 1
			k = k + 1

def quickSort(a) :
	quickSortBantu(a, 0, len(a) - 1 )

def quickSortBantu(a, awal, akhir) :
	if awal < akhir :
		titikBelah = partisi(a, awal, akhir)
		quickSortBantu(a, awal, titikBelah - 1)
		quickSortBantu(a, titikBelah + 1, akhir)

def partisi(a, awal, akhir) :
	nilaiPivot = a[awal]

	penandaKiri = awal + 1
	penandaKanan = akhir

	selesai = False
	while not selesai :
		while penandaKiri <= penandaKanan and a[penandaKiri] <= nilaiPivot :
			penandaKiri = penandaKiri + 1

		while a[penandaKanan] >= nilaiPivot and penandaKanan >= penandaKiri :
			penandaKanan = penandaKanan - 1

		if penandaKanan < penandaKiri :
			selesai = True
		else :
			temp = a[penandaKiri]
			a[penandaKiri] = a[penandaKanan]
			a[penandaKanan] = temp
	
	temp = a[awal]
	a[awal] = a[penandaKanan]
	a[penandaKanan] = temp

	return penandaKanan

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

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)


k = [i for i in range(1, 6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
u_mrg = k[:]
u_qck = k[:]

aw = detak();bubleSort(u_bub);ak=detak();print('Bubble Sort : %g detik' %(ak - aw));
aw = detak();insertionSort(u_ins);ak=detak();print('Insertion Sort : %g detik' %(ak - aw));
aw = detak();selectionSort(u_sel);ak=detak();print('Selection Sort : %g detik' %(ak - aw));
aw = detak();mergeSort(u_mrg);ak=detak();print('Merge Sort : %g detik' %(ak - aw));
aw = detak();quickSort(u_qck);ak=detak();print('Quick Sort : %g detik' %(ak - aw));

"""
Hasil dari semua algoritma yang dipelajari di jalankan :
Bubble Sort : 16.8512 detik
Insertion Sort : 6.90141 detik
Selection Sort : 5.46095 detik
Merge Sort : 0.117203 detik
Quick Sort : 0.074353 detik

algoritma QuickSort merupakan algoritma yang paling cepet dari semua algoritma yang dipelajari
"""
