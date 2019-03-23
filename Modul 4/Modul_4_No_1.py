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

#No 1
def CariIndexKota(kumpulan, k):
   ko = []
   for i in kumpulan :
      if i.kota == k :
         ko.append(kumpulan.index(i))
   return ko
