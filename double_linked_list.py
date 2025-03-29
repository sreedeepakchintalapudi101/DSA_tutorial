class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
        node.prev = itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print_forward(self):
        if not self.head:
            print("List is Empty")
            return
        itr = self.head
        fllstr = ""
        while itr:
            fllstr += str(itr.data) + " ---> "
            last_node = itr
            itr = itr.next
        print(f"Forward Linked List: {fllstr}")

    def print_backward(self):
        if not self.head:
            print("List is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        bllstr = ""
        while itr:
            bllstr += str(itr.data) + " <--- "
            itr = itr.prev
        print(f"Backward Linked List: {bllstr}")

    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data)
                node.next = itr.next
                node.prev = itr
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                return
            itr = itr.next
            count += 1

    def delete_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                if itr.prev:
                    itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                return
            itr = itr.next
            count += 1
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(5)
    dll.print_forward()
    dll.print_backward()
    dll.insert_at_index(2, 15)
    dll.print_forward()
    dll.delete_at_index(3)
    dll.print_forward()
    print(f"Length of DLL: {dll.get_length()}")
