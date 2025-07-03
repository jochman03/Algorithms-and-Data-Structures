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

def index_min(table):
    index_min = 0
    for i in range(len(table)):
        if table[i] < table[index_min]:
            index_min = i
    return index_min

def sort_shift(sort_table):
    table_size = len(sort_table)
    for i in range(0, table_size):
        m = index_min(sort_table[i:])
        elem = sort_table.pop(i+m)
        sort_table.insert(i, elem)


def sort_swap(sort_table):
    table_size = len(sort_table)
    for i in range(0, table_size):
        m = index_min(sort_table[i:])
        sort_table[i], sort_table[i+m] = sort_table[i+m], sort_table[i]

def TEST1():
    data = [ heap_element(value, key) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    new_heap = heap(data)
    new_heap.print_tab()    
    new_heap.print_tree(0, 0)
    while new_heap.is_empty() == False:
        new_heap.dequeue()
    print(data)
    print("NIESTABILNE")

    data_swap = [ heap_element(value, key) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    sort_swap(data_swap)
    print(data_swap)
    print("NIESTABILNE")

    data_shift = [ heap_element(value, key) for key,value in  [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]]
    sort_shift(data_shift)
    print(data_shift)
    print("STABILNE")

def TEST2():
    data_heap = list()
    data_swap = list()
    data_shift = list()

    for i in range(0,10000):
        number = int(random.random() * 100)
        data_heap.append(number)
        data_swap.append(number)
        data_shift.append(number)
    t_start = time.perf_counter()
    new_heap = heap(data_heap)
    while new_heap.is_empty() == False:
        new_heap.dequeue()
    t_stop = time.perf_counter()
    print("Czas obliczeń metoda kopcowa:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    sort_swap(data_swap)
    t_stop = time.perf_counter()
    print("Czas obliczeń metoda swap:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    sort_shift(data_shift)
    t_stop = time.perf_counter()
    print("Czas obliczeń metoda shift:", "{:.7f}".format(t_stop - t_start))

def main():
    try:
        test = int(input("Podaj numer testu (liczba całkowita o wartości 1 lub 2): "))
        
        if test == 1:
            TEST1()
        elif test == 2:
            TEST2()
        else:
            print("Nie ma takiego testu, wprowadź 1 lub 2.")
    except ValueError:
        print("To nie jest liczba całkowita")

if __name__ == '__main__':
    main()