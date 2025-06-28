class queue:
    def __init__(self):
        self._size = 5
        self._table = [None for i in range(self._size)]
        self._readIndex = 0
        self._writeIndex = 0
    def is_empty(self):
        return (self._readIndex == self._writeIndex)
    def peek(self):
        if self.is_empty():
            return None
        return self._table[self._readIndex]
    def dequeue(self):
        if self.is_empty():
            return None
        ret = self._table[self._readIndex]
        self._table[self._readIndex] = None
        self._readIndex += 1
        if self._readIndex == self._size:
            self._readIndex = 0
        return ret
    def enqueue(self, data):
        self._table[self._writeIndex] = data
        self._writeIndex += 1
        if self._writeIndex == self._size:
            self._writeIndex = 0
        if self._writeIndex == self._readIndex:
            new_size = self._size * 2
            self._table += [None for i in range(self._size)]
            for i, e in enumerate(reversed(range(self._readIndex, self._size))):
                self._table[-i - 1] = self._table[e]
                self._table[e] = None
            self._readIndex += self._size
            self._size = new_size
    def __str__(self):
        str = "["
        for i in range(self._readIndex, (self._size)):
            if(self._table[i] != None):
                str += f"{self._table[i]}, "
        for i in range(0, self._readIndex):
            if(self._table[i] != None):
                str += f"{self._table[i]}, "
        if not self.is_empty():
            str = str[:-2]                    
        str += "]"
        return str
    def print_table(self):
        print(self._table)

def main():
    que = queue()
    for i in range(1, 5):
        que.enqueue(i)
    print(que.dequeue())
    print(que.peek())
    print(que)
    for i in range(5, 9):
        que.enqueue(i)
    que.print_table()
    while not que.is_empty():
        print(que.dequeue())
    print(que)


if __name__ == '__main__':
    main()