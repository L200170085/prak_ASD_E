class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def _len__(self) :
        return len(self.qlist)

    def isEmpty(self):
        return len(self.qlist) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong."
        max = 0
        for i in range(len(self.qlist)):
            if self.qlist[i].priority < self.qlist[max].priority:
                max = i
        item = self.qlist[max]
        del self.qlist[max]
        return item

    def getFrontMost(self) :
        assert not self.isEmpty(), "Antrian sedang kosong."
        max = 0
        for i in range(len(self.qlist)):
            if self.qlist[i].priority < self.qlist[max].priority:
                max = i
        item = self.qlist[max]
        return item

    def getRearMost(self) :
        assert not self.isEmpty(), "Antrian sedang kosong."
        max = 0
        for i in range(len(self.qlist)):
            if self.qlist[i].priority > self.qlist[max].priority:
                max = i
        item = self.qlist[max]
        return item
    
class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority


p = PriorityQueue()
p.enqueue("mangga", 1)
p.enqueue("apel", 4)
p.enqueue("jeruk", 0)
p.enqueue("melon", 2)
print (p.getFrontMost().priority)
print (p.getRearMost().priority)
