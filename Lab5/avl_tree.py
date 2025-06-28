class tree_avl:
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
        self.root = self.root.insert(self.root, key, value)

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
        return self.root.a_height
    
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
        self.a_height = 1

    def update_height(self):
        left = 0
        right = 0
        if self.left_node != None:
            left = self.left_node.a_height
        if self.right_node != None:
            right = self.right_node.a_height
        self.a_height = max(left, right) + 1

    def get_balance(self):
        left = 0
        right = 0
        if self.left_node != None:
            left = self.left_node.a_height
        if self.right_node != None:
            right = self.right_node.a_height
        return left - right
    
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
        elif key > node.key:
            node.right_node = self.insert(node.right_node, key, value)
        else:
            node.value = value
            return node 
            
        node.update_height()
        balance = node.get_balance()
        if balance > 1:
            if node.left_node.get_balance() >= 0:
                return node.rotate_RR()
            else:
                node.left_node = node.left_node.rotate_LL()
                return node.rotate_RR()

        if balance < -1:
            if node.right_node.get_balance() <= 0:
                return node.rotate_LL()
            else:
                node.right_node = node.right_node.rotate_RR()
                return node.rotate_LL()

        return node

    def delete(self, node, key):
        if node == None:
            return node

        if key < node.key:
            node.left_node = self.delete(node.left_node, key)
        elif key > node.key:
            node.right_node = self.delete(node.right_node, key)
        else:
            if node.left_node == None and node.right_node == None:
                return None 
            elif node.left_node == None:
                return node.right_node
            elif node.right_node == None:
                return node.left_node

            smallest_left = node.right_node
            while smallest_left.left_node != None:
                smallest_left = smallest_left.left_node

            node.key = smallest_left.key
            node.value = smallest_left.value

            node.right_node = self.delete(node.right_node, smallest_left.key)

        node.update_height()
        balance = node.get_balance()

        if balance > 1:
            if node.left_node.get_balance() >= 0:
                return node.rotate_RR()
            else:
                node.left_node = node.left_node.rotate_LL()
                return node.rotate_RR()

        if balance < -1:
            if node.right_node.get_balance() <= 0:
                return node.rotate_LL()
            else:
                node.right_node = node.right_node.rotate_RR()
                return node.rotate_LL()

        return node

    def rotate_LL(self):    
        if self.right_node is None:
            return self
        B = self.right_node
        self.right_node = B.left_node
        B.left_node = self
        self.update_height()
        B.update_height()
        return B
    
    def rotate_RR(self):      
        if self.left_node is None:
            return self
        B = self.left_node
        self.left_node = B.right_node
        B.right_node = self
        self.update_height()
        B.update_height()
        return B

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
    new_tree = tree_avl()
    nodes = {50:'A', 15:'B', 62:'C', 5:'D', 2:'E', 1:'F', 11:'G', 100:'H', 7:'I', 6:'J', 55:'K', 52:'L', 51:'M', 57:'N', 8:'O', 9:'P', 10:'R', 99:'S', 12:'T'}
    for node in nodes.items():
        new_tree.insert(node[0], node[1])
    new_tree.print_tree()
    new_tree.print_sorted()
    print(new_tree.search(10))
    new_tree.delete(50)
    new_tree.delete(52)
    new_tree.delete(11)
    new_tree.delete(57)
    new_tree.delete(1)
    new_tree.delete(12)
    new_tree.insert(3, "AA")
    new_tree.insert(4, "BB")
    new_tree.delete(7)
    new_tree.delete(8)
    new_tree.print_tree()
    new_tree.print_sorted()

if __name__ == '__main__':
    main()
