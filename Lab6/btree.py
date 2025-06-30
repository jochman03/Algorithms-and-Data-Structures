class btree:
    def __init__(self, key_number):
        self.key_number = key_number
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = btree_element(self.key_number)
            self.root.keys[0] = key
            return
        result = self.root.insert(key)
        if result[0] != None:
            new_root = btree_element(self.key_number)
            new_root.keys[0] = result[1]
            if result[1] > self.root.keys[0]:
                new_root.children[0] = self.root
                new_root.children[1] = result[0]
            else:
                new_root.children[1] = self.root
                new_root.children[0] = result[0]
            self.root = new_root

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            for i in range(node.size+1): 	                	
                self._print_tree(node.children[i], lvl+1)
                if i<node.size:
                    print(lvl*'  ', node.keys[i])	

class btree_element:
    def __init__(self, key_number):
        self.size = key_number
        self.keys = [None for i in range(self.size)]
        self.children = [None for i in range(self.size + 1)]

    def insert(self, key):
        insert_index = None
        for i in range(self.size):
            if self.keys[i] == None or key < self.keys[i]:
                insert_index = i
                break
        if insert_index == None:
            insert_index = self.size

        if self.is_leaf():
            result = self.add_node(key, index=insert_index)
            if result[0] != None:
                return result[0], result[1]
            return None, None
        result = self.children[insert_index].insert(key)
        if result[0] != None:
            new_result = self.add_node(result[1], result[0])
            if new_result[0] != None:
                return new_result[0], new_result[1]
        return None, None

    def is_leaf(self):
        for i in range(self.size + 1):
            if self.children[i] != None:
                return False
        return True

    def is_full(self):
        for i in range(self.size):
            if self.keys[i] == None:
                return False
        return True

    def add_node(self, key, node=None, index=None):
        if not self.is_full():
            if index == None:
                index = 0
                while index < self.size and self.keys[index] != None and self.keys[index] < key:
                    index += 1
            for i in range(self.size - 1, index, -1):
                self.keys[i] = self.keys[i - 1]
            self.keys[index] = key

            if node != None:
                for i in range(self.size, index + 1, -1):
                    self.children[i] = self.children[i - 1]
                self.children[index + 1] = node
            return None, None

        all_keys = [k for k in self.keys if k != None]
        all_keys.append(key)
        all_keys.sort()

        mid_index = len(all_keys) // 2
        promoted_key = all_keys[mid_index]

        left_keys = all_keys[:mid_index]
        right_keys = all_keys[mid_index + 1:]

        new_node = btree_element(self.size)
        for i in range(len(right_keys)):
            new_node.keys[i] = right_keys[i]

        if any(self.children):
            all_children = []
            for child in self.children:
                if child != None:
                    all_children.append(child)
            if node != None:
                insert_pos = 0
                while insert_pos < len(all_keys) and key > all_keys[insert_pos]:
                    insert_pos += 1
                all_children.insert(insert_pos + 1, node)

            for i in range(len(all_children)):
                if i <= mid_index:
                    self.children[i] = all_children[i]
                else:
                    new_node.children[i - mid_index - 1] = all_children[i]

        self.keys = [None for l in range(self.size)]
        for i in range(len(left_keys)):
            self.keys[i] = left_keys[i]
        for i in range(len(self.children)):
            if i >= len(left_keys) + 1:
                self.children[i] = None

        return new_node, promoted_key
def main():
    tree1 = btree(3)
    for i in [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]:
        tree1.insert(i)
    tree1.print_tree()
    tree2 = btree(3)
    for i in range(20):
        tree2.insert(i)
    tree2.print_tree()
    for i in range(20, 200):
        tree2.insert(i)
    tree2.print_tree()
    tree3 = btree(5)
    for i in range(0, 200):
        tree3.insert(i)
    tree3.print_tree()

if __name__ == '__main__':
    main()