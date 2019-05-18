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

def cetakHexa(d):
    digit = "0123456789ABCDEF"
    f = Stack()
    if d == 0 :
        f.push(0)
    while d != 0 :
        sisa = d%16
        d = d//16
        f.push(digit[sisa])
    st = ""
    for i in range(len(f)):
        st = st + str(f.pop())
    return st

print (cetakHexa(255))
print (cetakHexa(100))
print (cetakHexa(2569))
