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

def quickSort(a) :
	quickSortBantu(a, 0, len(a) - 1 )

def quickSortBantu(a, awal, akhir) :
	if awal < akhir :
		titikBelah = partisi(a, awal, akhir)
		quickSortBantu(a, awal, titikBelah - 1)
		quickSortBantu(a, titikBelah + 1, akhir)

def partisi(a, awal, akhir) :
	nilaiPivot = a[awal].nim

	penandaKiri = awal + 1
	penandaKanan = akhir

	selesai = False
	while not selesai :
		while penandaKiri <= penandaKanan and a[penandaKiri].nim <= nilaiPivot :
			penandaKiri = penandaKiri + 1

		while a[penandaKanan].nim >= nilaiPivot and penandaKanan >= penandaKiri :
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
			

#list sebelum diurukan menggunakan Merge Sort
Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11]
print ("sebelum diurutkan")
#menampilkan list Daftar sebelum diurutkan
for i in Daftar:
    print (i.nim)


#diurutkan menggunakan Merge Sort
quickSort(Daftar)
#untuk menampilkan jika List Daftar sudah diurutkan
print("sesudah diurutkan")
for i in Daftar:
    print (i.nim)
