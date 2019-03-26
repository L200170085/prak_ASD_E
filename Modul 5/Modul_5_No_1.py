class Mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = uangsaku

m0 = Mahasiswa('Gentur Waskita', 85, 'Surakarta', 290000)
m1 = Mahasiswa('Ika', 10, 'Sukoharjo', 240000)
m2 = Mahasiswa('Ahmad', 2, 'Surakarta', 250000)
m3 = Mahasiswa('Chandra', 18, 'Surakarta', 235000)
m4 = Mahasiswa('Eka', 4, 'Boyolali', 240000)
m5 = Mahasiswa('Fandi', 31, 'Salatiga', 250000)
m6 = Mahasiswa('Deni', 13, 'Klaten', 245000)
m7 = Mahasiswa('Galuh', 5, 'Wonogiri', 245000)
m8 = Mahasiswa('Janto', 23, 'Klaten', 245000)
m9 = Mahasiswa('Hasan', 64, 'Karanganyar', 270000)
m10 = Mahasiswa('Khalid', 29, 'Purwodadi', 265000)
m11 = Mahasiswa('Budi', 51, 'Klaten', 210000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11]

def swap(a, b, c):
    a[b], a[c] = a[c], a[b]

def cariPosisiterkecil(a, darisini, sampaisini):
    posisiTerkecil = darisini
    for i in range(darisini+1, sampaisini):
        if a[i].nim < a[posisiTerkecil].nim:
            posisiTerkecil = i
    return posisiTerkecil

def bubleSort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j].nim > a[j+1].nim:
                swap(a, j, j+1)

def selectionSort(a):
    n = len(a)
    for i in range(n-1):
        indexKecil = cariPosisiterkecil(a, i, n)
        if indexKecil != i :
            swap(a, i, indexKecil)

selectionSort(Daftar)
"""untuk menampilkan data yang telah diurutkan."""
for i in range(0, len(Daftar)-1):
    print (Daftar[i].nim)
