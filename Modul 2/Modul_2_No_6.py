class Manusia(object):
    """ Class 'Manusia' dengan inisiasi 'nama' """
    keadaan = 'Lapar'
    def __init__(self, nama):
        self.nama = nama

    def ucapkanSalam(self):
        print ("Salam, namaku",self.nama)

    def makan(self, s):
        print ("Saya baru saja makan", s)
        self.keadaan = 'kenyang'

    def olahraga(self, k):
        print ("Saya baru saja latihan", k)
        self.keadaan = 'Lapar'

    def mengalikanDenganDua(self, n):
        return n * 2

class SiswiSMA(Manusia):
    """ Class 'SiswiSMA' merupakan class turunan dari class 'Manusia' """
    def __init__(self, nama, alamat, nip, jurusan):
        self.nama = nama
        self.alamat = alamat
        self.nip = nip
        self.jurusan = jurusan

    def __str__(self):
        a = self.nama + ' bertempat tinggal di ' +self.alamat+ ', mempunyai NIP '+str(self.nip)+' dan mengambil jurusan '+self.jurusan+'.'
        return a
