class Stack(object):
    def __init__(self) :
        self.item = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.item)

    def peek(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa Diintip."
        return self.item[-1]

    def pop(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa di-Pop."
        return self.item.pop()

    def push(self, data):
        self.item.append(data)


nilai = Stack()
for i in range(16):
    if i % 3 == 0 :
        nilai.push(i)
        
print (nilai.item)

##akan menghasilkan
##[0, 3, 6, 9, 12, 15]
##langkah jika dieksekusi :
##0 simpan i = 0 -> nilai = [0]
##1 tidak memenuhi kondisi
##2 tidak memenuhi kondisi
##3 simpan i = 3 -> nilai = [0, 3]
##4 tidak memenuhi kondisi
##5 tidak memenuhi kondisi
##6 simpan i = 6 -> nilai = [0, 3, 6]
##7 tidak memenuhi kondisi
##8 tidak memenuhi kondisi
##9 simpan i = 9 -> nilai = [0, 3, 6, 9]
##10 tidak memenuhi kondisi
##11 tidak memenuhi kondisi
##12 simpan i = 12 -> nilai = [0, 3, 6, 9, 12]
##13 tidak memenuhi kondisi
##14 tidak memenuhi kondisi
##15 simpan i = 15 -> nilai = [0, 3, 6, 9, 12, 15]
