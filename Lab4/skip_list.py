import random


class skip_list:
    def __init__(self, max_levels):
        self.max_levels = max_levels
        self.head = skip_list_element("head", None, self.max_levels, 1)

    def search(self, key):
        node = self.head
        for i in range(self.max_levels - 1, -1, -1):
            while node.tab[i] and node.tab[i].key < key:
                node = node.tab[i]

        node = node.tab[0]
        if node and node.key == key:
            return node.data
        return None

    def insert(self, key, data):
        self.remove(key)
        node = self.head
        prev_table = [None for i in range(0, self.max_levels)]
        for i in range(self.max_levels - 1, -1, -1):
            while node.tab[i] and node.tab[i].key < key:
                node = node.tab[i]
            prev_table[i] = node 
        
        new_node = skip_list_element(key, data, self.max_levels)
        for i in range(new_node.levels):
            new_node.tab[i] = prev_table[i].tab[i]
            prev_table[i].tab[i] = new_node

    def remove(self, key):
        node = self.head
        prev_table = [None for i in range(0, self.max_levels)]

        for i in range(self.max_levels - 1, -1, -1):
            while node.tab[i] != None and node.tab[i].key < key:
                node = node.tab[i]
            prev_table[i] = node

        taget_node = node.tab[0] 
        if taget_node != None and taget_node.key == key:
            for i in range(self.max_levels):
                if prev_table[i].tab[i] == taget_node:
                    prev_table[i].tab[i] = taget_node.tab[i]

    
        
    def __str__(self):
        node = self.head.tab[0]
        str = "[ "
        while node != None:
            str += f"{node.key}:{node.data} "
            node = node.tab[0]
        str += "]"
        return str
    
    def displayList_(self):
        node = self.head.tab[0]
        keys = [ ]                       
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.max_levels - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.data:2s}", end="")
                node = node.tab[lvl]
            print()
class skip_list_element:
    def __init__(self, key, data, max_levels, is_head=0):
        self.key = key
        self.data = data
        self.max_levels = max_levels
        self.levels = 0

        if is_head:
            self.levels = max_levels
        else:
            self.levels = self.randomLevel(0.5, self.max_levels)
        
        self.tab = [None for i in range(0, self.levels)]

    def randomLevel(self, p, maxLevel):
        lvl = 1

        while random.random() < p and lvl < maxLevel:

            lvl = lvl + 1

        return lvl

def main():
    random.seed(42)
    sl = skip_list(5)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(1, 16):
        sl.insert(i, letters[i - 1])
    sl.displayList_()
    print(sl.search(2))
    sl.insert(2, 'Z')
    print(sl.search(2))
    for i in [5, 6, 7]:
        sl.remove(i)
    print(sl)
    sl.insert(6, 'W')
    print(sl)

    sl = skip_list(5)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(15, 0, -1):
        sl.insert(i, letters[i - 1])
    sl.displayList_()
    print(sl.search(2))
    sl.insert(2, 'Z')
    print(sl.search(2))
    for i in [5, 6, 7]:
        sl.remove(i)
    print(sl)
    sl.insert(6, 'W')
    print(sl)

if __name__ == '__main__':
    main()