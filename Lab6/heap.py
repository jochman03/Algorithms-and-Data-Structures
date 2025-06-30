class heap_element:
    def __init__(self, value, priority):
        self._priority = priority
        self._value = value
    def get_value(self):
        return self._value
    def get_priority(self):
        return self._priority
    def __lt__(self, other):
        return self._priority < other.get_priority()
    def __gt__(self, other):
        return self._priority > other.get_priority()
    def __repr__(self):
        return f"{self._priority}: {self._value}"
class heap:
    def __init__(self):
        self._table = list()
        self._size = 0
    def left(self, i):
        return 2 * i + 1
    def right(self, i):
        return 2 * i + 2
    def parent(self, i):
        return (i - 1) // 2
    def is_empty(self):
        return self._size == 0
    def peek(self):
        if self.is_empty():
            return None
        return self._table[0]
    def dequeue(self):
        if self.is_empty():
            return None
        return_value = self._table[0]
        self._table[0], self._table[self._size - 1] = self._table[self._size - 1], self._table[0]
        self._size -= 1
        if self._size == 0:
            return return_value
        self.repair()
        return return_value

    def repair(self, i=0):
        while i < self._size:
            left = self.left(i)
            right = self.right(i)
            if left >= self._size:
                break
            if right >= self._size:
                right = None
            if right == None:
                if self._table[left] > self._table[i]:
                    self._table[left], self._table[i] = self._table[i], self._table[left]
                    i = left
                    continue
                else:
                    return
            if self._table[left] > self._table[right]:
                if self._table[left] > self._table[i]:
                    self._table[left], self._table[i] = self._table[i], self._table[left]
                    i = left
                    continue
                else:
                    return
            else:
                if self._table[right] > self._table[i]:
                    self._table[right], self._table[i] = self._table[i], self._table[right]
                    i = right
                    continue
                else:
                    return
        return
    def enqueue(self, element):
        if self._size == len(self._table):
            self._table.append(element)
        else:
            self._table[self._size] = element
        self._size += 1
        i = self._size - 1
        while i > 0:
            parent = self.parent(i)
            if self._table[parent] < self._table[i]:
                self._table[parent], self._table[i] = self._table[i], self._table[parent]
                i = parent
            else:
                break
    def print_tab(self):
        print('{', end=' ')
        print(*self._table[:self._size], sep=', ', end=' ')
        print('}')
    def print_tree(self, idx, lvl):
        if idx < self._size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2*lvl*' ', self._table[idx] if self._table[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


def main():
    new_heap = heap()
    priorities = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    text = "GRYMOTYLA"
    for i in range(0, 9):
        new_heap.enqueue(heap_element(text[i], priorities[i]))
    new_heap.print_tree(0, 0)
    new_heap.print_tab()

    first = new_heap.dequeue()
    print(new_heap.peek())
    new_heap.print_tab()
    print(first)
    while new_heap.is_empty() == False:
        print(new_heap.dequeue())
    new_heap.print_tab()

if __name__ == '__main__':
    main()