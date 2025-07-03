import time
import random
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
    def __init__(self, sort_table = None):
        if sort_table != None:
            self._table = sort_table
            self._size = len(sort_table)
            for i in range(self._size, -1, -1):
                if self.left(i) < self._size and self.right(i) < self._size:
                    if self._table[self.left(i)] != None and self._table[self.right(i)] != None:
                        self.repair(i) 
        else:
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



def insertion_sort(table):
    for i in range(1, len(table)):
        j = i - 1 
        ti = table[i] 
        while table[j] > ti:
            table[j + 1] = table[j]
            j -= 1  
            if j < 0:
                break
        table[j + 1] = ti

def shell_sort(table):
    k = 1
    while (3*k - 1)//2 < len(table)//3:
        k = k + 1
    h = (3*k - 1)//2
    while h > 0:
        for i in range(h, len(table)):  
            ti = table[i]
            j = i
            while table[j - h] > ti:
                table[j] = table[j - h]
                j = j - h
                if j < h:
                    break
            table[j] = ti  
        h = h // 3

def main():
    data_insert = [ heap_element(value, key) for key,value in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')] ]
    data_shell = [ heap_element(value, key) for key,value in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')] ]

    insertion_sort(data_insert)
    print(data_insert)
    print("STABILNE")

    shell_sort(data_shell)
    print(data_shell)
    print("NIESTABILNE")

    data_heap = list()
    data_insert = list()
    data_shell = list()

    for i in range(0,10000):
        number = int(random.random() * 100)
        data_heap.append(number)
        data_insert.append(number)
        data_shell.append(number)

    compare = list()

    t_start = time.perf_counter()
    new_heap = heap(data_heap)
    while new_heap.is_empty() == False:
        new_heap.dequeue()
    t_stop = time.perf_counter()
    t_heap = t_stop - t_start
    print("Czas sortowania kopcowego: ", t_heap)
    compare.append(heap_element("Sortowanie kopcowe", t_heap))

    t_start = time.perf_counter()
    insertion_sort(data_insert)
    t_stop = time.perf_counter()
    t_insert = t_stop - t_start
    print("Czas sortowania poprzez wstawianie: ", t_insert)
    compare.append(heap_element("Sortowanie poprzez wstawianie", t_insert))

    t_start = time.perf_counter()
    shell_sort(data_shell)
    t_stop = time.perf_counter()
    t_shell = t_stop - t_start
    print("Czas sortowania metodą Shella: ", t_shell)

    compare.append(heap_element("Sortowanie metodą Shella", t_shell))

    shell_sort(compare)

    print("\n")
    print("Porównanie czasu sortowania:")
    for element in compare:
        print(element.get_value(), end="")
        if element != compare[-1]:
            print(" < ", end="")
    print("")
    for element in compare:
        print(element.get_priority(), end="")
        if element != compare[-1]:
            print(" < ", end="")

if __name__ == '__main__':
    main()