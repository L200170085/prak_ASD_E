import Modul_2_No_2

class MhsTIF(Modul_2_No_2.Mahasiswa):
    """ Class 'MhsTIF' dibangun dari class 'Mahasiswa'"""
    def katakanPy(self):
        print ('Python is cool...')


"""
Setiap state atau method yang dipanggil dari Object yang dibuat dari Class MhsTIF
semuanya berasal dari Class Manusia, Mahasiswa, dan Class itu sendiri MhsTIF. Karena
Class MhsTIF merupakan inheritence dari Class Manusia dan Mahasiswa sehingga mewarisi semua
properti dan method yang dimiliki Class induk.

"""
