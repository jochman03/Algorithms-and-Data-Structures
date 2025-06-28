class tree:
    def __init__(self):
        self.root = None
    def search(self, key):
        if self.root == None:
            return None
        return self.root.search(key)
    def insert(self, key, value):
        if self.root == None:
            self.root = tree_node(key, value)
            return 1
        self.root.insert(self.root, key, value)
    def delete(self, key):
        if self.root == None:
            return None
        self.root = self.root.delete(self.root, key)
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")
    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right_node, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left_node, lvl+5)
    def height(self):
        if self.root == None:
            return 0
        return self.root.height(1)
    def print_sorted(self):
        if self.root == None:
            print("")
            return
        print(self.root.print_sorted())
class tree_node:
    def __init__(self, key, value, left_node=None, right_node=None):
        self.key = key
        self.value = value
        self.left_node = left_node
        self.right_node = right_node
    def search(self, key):
        if self.key == key:   
            return self.value

        if self.key > key:
            if self.left_node != None:
                return self.left_node.search(key)
            return None
        if self.key < key: 
            if self.right_node != None: 
                return self.right_node.search(key)
        return None
    def insert(self, node, key, value):
        if node == None:
            return tree_node(key, value)
        if key < node.key:
            node.left_node = self.insert(node.left_node, key, value)
            return node
        elif key > node.key:
            node.right_node = self.insert(node.right_node, key, value)
            return node
        node.value = value
        return node
    def delete(self, node, key):
        if node.key > key:
            if node.left_node != None:
                node.left_node = self.delete(node.left_node, key)
                return node
        if node.key < key:
            if node.right_node != None:
                node.right_node = self.delete(node.right_node, key)
                return node
        if node.key == key:
            if node.left_node is None and node.right_node is None:
                return None
            if node.left_node is None:
                return node.right_node
            if node.right_node is None:
                return node.left_node
            
            smallest_left = node.right_node
            while smallest_left.left_node != None:
                smallest_left = smallest_left.left_node
            temp_key =smallest_left.key
            node.value = smallest_left.value
            self.delete(self, smallest_left.key)
            node.key = temp_key
            return node
    def height(self, actual_height):
        if (self.left_node == None) and (self.right_node == None):
            return actual_height
        left = 0
        right = 0
        if self.left_node != None:
            left = self.left_node.height(actual_height + 1)
        if self.right_node != None:
            right = self.right_node.height(actual_height + 1)
        if left > right:
            return left
        return right
    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right_node, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
        
            self.__print_tree(node.left_node, lvl+5)
    def print_sorted(self):
        str = ""
        if self.left_node != None:
            str += self.left_node.print_sorted()
        str += f"{self.key} {self.value}, "
        if self.right_node != None:
            str += self.right_node.print_sorted()
        return str


def main():
    new_tree = tree()
    nodes = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for node in nodes.items():
        new_tree.insert(node[0], node[1])
    new_tree.print_tree()
    new_tree.print_sorted()
    print(new_tree.search(24))
    new_tree.insert(20, "AA")
    new_tree.insert(6, "M")
    new_tree.delete(62)
    new_tree.insert(59, "N")
    new_tree.insert(100, "P")
    new_tree.delete(8)
    new_tree.delete(15)
    new_tree.insert(55, "R")
    new_tree.delete(50)
    new_tree.delete(5)
    new_tree.delete(24)
    print(new_tree.height())
    new_tree.print_sorted()
    new_tree.print_tree()

if __name__ == '__main__':
    main()