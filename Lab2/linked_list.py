class Element:
    def __init__(self, tuple):
        self.data = tuple[0]
        self.next = tuple[1]

class Linked_List:
    def __init__(self):
        self.head = None
    def destroy(self):
        self.head = None
    def add(self, data):
        element = Element((data, None))
        if(self.head != None):
            element.next = self.head
        self.head = element
    def append(self, data):
        if (self.head == None):
            self.head = Element((data, None))
            return
        element = self.head
        while element.next != None:
            element = element.next
        element.next = Element((data, None))
    def remove(self):
        if(self.head == None):
            return
        self.head = self.head.next
    def remove_end(self):
        if(self.head == None) or (self.head.next == None) :
            self.head = None
            return
        element = self.head
        while element.next.next != None: 
            element = element.next
        element.next = None
            
    def __str__(self):
        if(self.head != None):
            text = ""
            element = self.head
            while element != None:
                text += f"{element.data}\n"
                element = element.next
            return text
        else:
            return "None"
    def is_empty(self):
        if(self.head == None):
            return True
        return False
    def length(self):
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
    
def main():
    uczelnie = Linked_List()
    table = [('AGH', 'Kraków', 1919),('UJ', 'Kraków', 1364),('PW', 'Warszawa', 1915),('UW', 'Warszawa', 1915),('UP', 'Poznań', 1919),('PG', 'Gdańsk', 1945)]
    for tuple in table[:3]:
        uczelnie.append(tuple)
    for tuple in table[3:6]:
        uczelnie.add(tuple)
    print(uczelnie)
    print(uczelnie.length())
    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.remove_end()
    uczelnie.append(('AGH', 'Kraków', 1919))
    uczelnie.remove_end()
    print(uczelnie.is_empty())

if __name__ == '__main__':
    main()