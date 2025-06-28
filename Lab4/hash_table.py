class hash_table_element:
    def __init__(self, key, data):
        self.key = key
        self.data = data
    def __str__(self):
        return f"{self.key}:{self.data}"


class hash_table:
    def __init__(self, size, c1 = 1, c2 = 0):
        self._tab = [None for i in range(size)]
        self._size = size
        self._c1 = c1
        self._c2 = c2
    def hash(self, key):
        if isinstance(key, str) and key.isalpha(): 
            key = sum(ord(i) for i in key)
        index = key % self._size
        return index
    def addres_collision(self, index):
        i = 1
        while i < self._size:
            new_index = (index + self._c1 * i + self._c2 * (i ** 2)) % self._size
            if self._tab[new_index] == None or self._tab[new_index] == "DELETED":
                return new_index
            i += 1
        return None
    def search(self, key):
        index = self.hash(key)
        i = 0
        while i < self._size:
            new_index = (index + self._c1 * i + self._c2 * (i ** 2)) % self._size
            if self._tab[new_index] is None:
                break
            if self._tab[new_index] != "DELETED" and self._tab[new_index].key == key:
                return self._tab[new_index].data
            i += 1
        return None
    def insert(self, key, data):
        index = self.hash(key)
        if self._tab[index] != None and self._tab[index] != "DELETED":
            if self._tab[index].key == key:
                self._tab[index].data = data
                return
            new_index = self.addres_collision(index)
            if new_index == None:
                raise KeyError("Brak miejsca")
            index = new_index
        self._tab[index] = hash_table_element(key, data)
    def remove(self, key):
        index = self.hash(key)
        i = 0
        while i < self._size:
            new_index = (index + self._c1 * i + self._c2 * (i ** 2)) % self._size
            if self._tab[new_index] != None and self._tab[new_index].key == key:
                self._tab[new_index] = "DELETED"
                return
            i += 1
        raise KeyError("Brak danej")
    def __str__(self):
        str = "["
        for element in self._tab:
            if element == None or element == "DELETED":
                str += f"None, "
            else:
                str += f"{element}, "
        str += "]"
        return str

def test_function1(c1 = 1, c2 = 0):
    tab = hash_table(13, c1, c2)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(1, 16):
        index = i - 1
        if i == 6:
            i = 18
        elif i == 7:
            i = 31
        try:
            tab.insert(i, letters[index])
        except KeyError:
            pass
    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    tab.insert(5, 'Z')
    print(tab.search(5))
    tab.remove(5)
    print(tab)
    print(tab.search(31))
    tab.insert("test", 'W')
    print(tab)

def test_function2(c1 = 1, c2 = 0):
    tab = hash_table(13, c1, c2)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(1, 16):
        index = i - 1
        i = i * 13
        try:
            tab.insert(i, letters[index])
        except KeyError:
            pass
    print(tab)

def main():
    test_function1()
    test_function2(1, 0)
    test_function2(0, 1)
    test_function1(0, 1)
    
if __name__ == '__main__':
    main()