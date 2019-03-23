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

def CariIndexKota(kumpulan, k):
   ko = []
   for i in kumpulan :
      if i.kota == k :
         ko.append(kumpulan.index(i))
   return ko


def UangSakuTerkecil(kumpulan) :
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
    return terkecil

def DaftarSakuTerkecil(kumpulan) :
    kecil = []
    terkecil = kumpulan[0].uangsaku
    for i in kumpulan :
        if i.uangsaku < terkecil :
            terkecil = i.uangsaku
            kecil.append(kumpulan.index(i))
    return kecil

def DaftarSakuKecil(kumpulan):
    kecil = []
    for i in kumpulan :
        if i.uangsaku < 250000 :
            kecil.append(kumpulan.index(i))
    return kecil

#No 6
def binary_search(kumpulan, target):
    jml = []
    kiri = 0
    kanan = len(kumpulan) - 1

    while kiri <= kanan :
        mid = (kiri + kanan) // 2
        if kumpulan[mid] == target :
            jml.append(kumpulan.index(target))
            return jml
        elif target < kumpulan[mid]:
            kanan = mid - 1
        else :
            kiri = mid + 1
    return False

d = [1, 2, 3, 3, 4, 5, 5, 5, 5, 133, 134, 157, 157, 189, 200, 230, 235,345]
