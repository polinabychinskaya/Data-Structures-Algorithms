class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # If the list is not empty, a new node is created 
    # with the given data, and its next is set to 
    # the current head. The prev of the current head 
    # is then updated to reference the new node. 
    # Finally, the head is updated to point to the new node
    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node


    def print_forward(self):
        if self.head is None:
            print('Doubly linked list is empty')
            return 
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_begining('one')
    ll.insert_at_begining('two')
    ll.print_forward()
    ll.print_backward()