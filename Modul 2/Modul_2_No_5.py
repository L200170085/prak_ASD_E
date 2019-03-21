import Modul_2_No_6

class Mahasiswa(Modul_2_No_6.Manusia):
    """Class 'Mahasiswa' yang dibangun dari kelas 'Manusia' """
    list_kuliah = []
    def __init__(self, nama, NIM, kota, saku):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia. """
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.saku = saku
        
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) + '. Tinggal di '+ self.kotaTinggal + '. Uang saku Rp. '+ str(self.saku) + ' tiap bulannya.'
        return s

    def ambilNama(self):
        return self.nama

    def ambilNIM(self):
        return self.NIM

    def ambilSaku(self):
        return self.saku

    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia. Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan ",s,"sambil belajar.")
        self.keadaan = 'kenyang'

    def ambilKotaTinggal(self):
        return self.kotaTinggal

    def perbaruiKotaTinggal(self, perbarui):
        self.kotaTinggal = perbarui

    def tambahUangSaku(self, tambah):
        self.saku = self.saku + tambah
        return self.saku

    def ambilKuliah(self, ambil):
        self.list_kuliah.append(ambil)

    # No 5
    def hapusKuliah(self, hapus):
        self.list_kuliah.remove(hapus)
