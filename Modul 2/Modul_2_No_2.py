import Modul_2_No_6

class Mahasiswa(Modul_2_No_6.Manusia):
    """Class 'Mahasiswa' yang dibangun dari kelas 'Manusia' """

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

    #No. 2 a
    def ambilKotaTinggal(self):
        return self.kotaTinggal

    #No. 2 b
    def perbaruiKotaTinggal(self, k):
        self.kotaTinggal = k

    #No. 2 c
    def tambahUangSaku(self, t):
        self.saku = self.saku + t
        return self.saku
