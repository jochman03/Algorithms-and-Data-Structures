
list_size = 6
class unrolled_linked_list_element:
    def __init__(self):
        self.table = [None for i in range(list_size)]
        self.filled = 0
        self.next = None
    def insert(self, index, data):
        create_new = 0
        if  index < 0:
            return None
        if index >= list_size:
            i = None
            for e in range(0, list_size):
                if self.table[e] == None:
                    i = e
                    break
            if i == None:
                i = list_size - 1
            index = i
            create_new = 1
        if self.filled < list_size:
            if self.table[index] != None:
                new_table = [None for i in range(list_size)]
                for i in range(index, list_size-1):
                    new_table[i+1] = self.table[i]
                if index != 0:
                    for i in range(0, index):
                        new_table[i] = self.table[i]
                new_table[index] = data
                self.table = new_table
                self.filled += 1
                return
            
            self.table[index] = data
            self.filled += 1
            return
        else: 
            if self.next == None:
                self.next = unrolled_linked_list_element()
            else:
                temp = self.next
                self.next = unrolled_linked_list_element()
                self.next.next = temp
            for i in range(0, round(list_size/2)):
                temp = self.table[round(list_size/2) + i]
                self.table[round(list_size/2) + i] = None
                self.next.table[i] = temp
            self.filled = round(list_size/2)
            self.next.filled = round(list_size/2)
            if index > round(list_size/2):
                self.next.insert(index - round(list_size/2) + create_new, data)
                return
            self.insert(index, data)
            return
        


        
            
    def delete(self, index):
        if (index >= list_size) or (index < 0):
            return None
        for i in range(index, list_size - 1):
            self.table[i] = self.table[i+1]
            self.table[list_size - 1] = None
        self.filled -= 1
        if (self.filled < round(list_size/2)) and (self.next != None):
            if self.next.filled <= round(list_size/2):
                for i in range(0, round(list_size/2)):
                    self.insert(list_size, self.next.table[i])
                self.next = self.next.next
                return
            self.insert(10, self.next.table[0])
            self.next.delete(0)

class unrolled_linked_list:
    def __init__(self):
        self._head = unrolled_linked_list_element()
        self.filled = 0
    def __str__(self):
        element = self._head
        str = "["
        index = 0
        while element != None:
            for i in element.table:
                if i != None:
                    str += f"{i}"
                    index += 1
                    if index != self.filled:
                        str += ", "
            element = element.next
        str += "]"
        return str
    def get(self, index):
        element = self._head
        i = 0
        while element != None:
            for e in element.table:
                if e != None:
                    if i == index:
                        return e
                    i += 1
            element = element.next
        return None
    def insert(self, index, data):
        if index > self.filled: 
            element = self._head
            while element != None:
                if element.next == None:
                    element.insert(list_size+1, data)
                    self.filled += 1
                element = element.next
            return
        element = self._head 
        i = 0
        i_element = 0
        last_element = None
        while element != None:
            for e in range(0, list_size):
                if e != (list_size - 1) and (element.table[e] != None) :
                    if (element.table[e + 1] == None) and (index == (i + 1)):
                        element.insert(e + 1, data)
                        self.filled += 1
                        return
                if index == i:
                    element.insert(e, data)
                    self.filled += 1
                    return
                if (element.table[e] != None):
                    i += 1
            last_element = element    
            i_element += element.filled
            element = element.next
        last_element.insert(list_size+1, data)
        self.filled += 1
        return
    

    def delete(self, index):
        if (index > self.filled) or (self.filled == 0):
            return None
        element = self._head  
        i = 0
        last_element = None
        while element != None:
            for e in range(0, list_size):
                if element.table[e] == None:
                    break
                if i == index:
                    if(element.filled == 1):
                        last_element.next = None
                        return       
                    element.delete(e)
                    self.filled -= 1
                    return
                i += 1
            last_element = element
            element = element.next
        
        return

def main():
    list_size = 6

    tab = unrolled_linked_list()
    for i in range(1, 10):
        tab.insert(i-1, i)
    print(tab.get(4))
    tab.insert(1, 10)
    tab.insert(8, 11)
    print(tab)
    tab.delete(1)
    tab.delete(2)
    print(tab)
    
if __name__ == '__main__':
    main()