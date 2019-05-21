class Queue(object) :
    def __init__(self) :
        self.qlist = []

    def isEmpty(self) :
        return len(self) == 0

    def __len__(self) :
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong."
        return self.qlist.pop(0)

    def getFrontMost(self):
        return self.qlist[0]

    def getRearMost(self):
        return self.qlist[-1]

q = Queue()
q.enqueue(10)
q.enqueue(4)
q.enqueue(3)
q.enqueue(18)
print (q.getFrontMost())
print (q.getRearMost())
