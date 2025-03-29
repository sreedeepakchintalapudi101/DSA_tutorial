class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self,data):
        node = Node(data,None)
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head = node
        
    def print(self):
        if not self.head:
            print("Linked List is empty")
            return
        llstr = ""
        itr = self.head
        while itr:
            llstr = llstr + str(itr.data) + "--->"
            itr = itr.next
        print(llstr)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        print(f"The count is {count}")
        return count
    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    def insert_at_index(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
            return
        if index == 0:
            self.head = Node(data, None)
            return
        count = 0
        itr = self.head
        while itr:
            if index == count - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count + 1
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
            return
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if index == count - 1:
                itr.next = itr.next.next
                break
            count = count + 1
            
    def insert_values(self, data_list):
        self.head = None  # Reset the list
        for data in data_list:
            self.insert_at_end(data)
if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert_values([10, 20, 30])
    l1.print()
    l1.insert_at_end(40)
    l1.print()
    l1.insert_at_beginning(5)
    l1.print()
    l1.insert_at_index(25,3)
    l1.print()
    l1.remove_at(2)
    l1.print()
