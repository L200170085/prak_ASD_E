class Pesan(object):
    """Sebuah class bernama Pesan.
        Untuk memahami class dan object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString

    def cetakIni(self):
        print(self.teks)

    def cetakPakaiHurufKapital(self):
        print (str.upper(self.teks))

    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))

    def jumlahKarakter(self):
        return len(self.teks)

    def cetakJumlahKarakterku(self):
        print ("Kalimatku mempunyai",len(self.teks), 'karakter.')

    def perbarui(self, stringBaru):
        self.teks = stringBaru

    def apakahTerkandung(self, a):
        if a in self.teks :
            print (True)
        else :
            print (False)

    def hitungKonsonan(self):
        vokal = 'AIUEOaiueo'
        konsonan = 0
        for i in range (len(self.teks)):
            if self.teks[i] not in vokal :
                konsonan += 1
        return konsonan

    def hitungVokal(self):
        vokal = 'AIUEOaiueo'
        jml_vokal = 0
        for i in range (len(self.teks)):
            if self.teks[i] in vokal :
                jml_vokal += 1
        return jml_vokal
