class Element:
    def __init__(self, tuple):
        self.data = tuple[0]
        self.next = tuple[1]
        self.prev = tuple[2]
    def print(self):
        prev_data = "None"
        data = self.data
        next_data = "None"
        if self.prev != None:
            prev_data = self.prev.data
        if self.next != None:
            next_data = self.next.data           
        return f"{prev_data} -> {data} -> {next_data}"

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    def destroy(self):
        element = self.head
        while element.next != None:
            element.tail = None
            element = element.next
        self.head = None
        self.tail = None
    def add(self, data):
        element = Element((data, None, None))
        if(self.head != None):
            self.head.prev = element
            element.next = self.head
        else:
            self.tail = element
        self.head = element
    def append(self, data):
        if (self.head == None):
            element = Element((data, None, None)) 
            self.head = element
            self.tail = element
            return
        element = self.head
        while element.next != None:
            element = element.next
        element.next = Element((data, None, element))
        self.tail = element.next
    def remove(self):
        if(self.head == None):
            return
        if(self.head.next == None):
            self.tail = None
        self.head = self.head.next
        self.head.prev = None
    def remove_end(self):   #FIXME
        if(self.head == None) or (self.head.next == None) :
            self.head = None
            self.tail = None
            return
        element = self.head
        while element.next.next != None: 
            element = element.next
        element.next = None
        self.tail = element
            
    def __str__(self):  #FIXME
        if(self.head != None):
            text = ""
            element = self.head
            while element != None:
                text += f"{element.data}\n"
                element = element.next
            return text
        else:
            return "None"
    def is_empty(self):   #FIXME
        if(self.head == None):
            return True
        return False
    def length(self):   #FIXME
        if(self.head == None):
            return 0
        element = self.head
        count = 1
        while element.next != None:
            count += 1
            element = element.next
        return count
    def get(self):
        if(self.head == None):
            return
        return self.head.data
    def print_backwards(self):
        if(self.tail == None):
            print("None")
        element = self.tail
        while element != None:
            print(f"{element.data}")
            element = element.prev
    def debug(self):
        element = self.head
        while element != None:
            print(element.print(),"\n")
            element = element.next
def main():
    uczelnie = Linked_List()
    table = [('AGH', 'Kraków', 1919),('UJ', 'Kraków', 1364),('PW', 'Warszawa', 1915),('UW', 'Warszawa', 1915),('UP', 'Poznań', 1919),('PG', 'Gdańsk', 1945)]
    for tuple in table[:3]:
        uczelnie.append(tuple)
    for tuple in table[3:6]:
        uczelnie.add(tuple)
    print(uczelnie)
    uczelnie.print_backwards()
    print("\n\n")
    uczelnie.debug()
    print("\n\n")

    print(uczelnie.length())
    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.print_backwards()

    print("\n\n")
    uczelnie.debug()
    print("\n\n")

    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.remove_end()
    uczelnie.append(('AGH', 'Kraków', 1919))
    uczelnie.remove_end()
    print(uczelnie.is_empty())
 

if __name__ == '__main__':
    main()