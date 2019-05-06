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
			if separuhKiri[i].nim < separuhKanan[j].nim :
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

	# print ("Menggabungkan", a)

#list sebelum diurukan menggunakan Merge Sort
Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11]
print ("sebelum diurutkan")
#menampilkan list sebelum diurutkan
for i in Daftar:
    print (i.nim)


#diurutkan menggunakan Merge Sort
mergeSort(Daftar)
#untuk menampilkan jika List Daftar sudah diurutkan
print("sesudah diurutkan")
for i in Daftar:
    print (i.nim)
