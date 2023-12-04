# Element of the linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        # Pointer to the next element (link)
        self.next = next 

class LinkedList:
    def __init__(self):
        # Head of the linked list
        self.head = None 
    
    def insert_at_begining(self, data):
        # Here we have self.head as 'next' because the current 
        # first element will be the second one after insertion 
        node = Node(data, self.head) 
        self.head = node

    def print(self):
        # If there is no 1st element (head), then ..
        if self.head is None:
            print('Linked list is empty')
            return 
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            # If there is no head, the data for 
            # the node will be attached to the head data
            self.head = Node(data, None)
            return

        itr = self.head
        # If it has a value inside, you are not at the end
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid input')
        if index == 0:
            # If you remove the head element, 
            # the next one becomes the head
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        # If you want to remove the element, 
        # you have to modify the link of the elements,
        # which is prior to the deleted one
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid input')
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            # Here, we refer to the node which goes before the new one
            if count == index - 1:
                # Here, we create a new node
                node = Node(data, itr.next)
                # Because here we want to modify the former link
                itr.next = node
                break
            itr = itr.next
            count += 1
        
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") 
    ll.print()
    ll.remove_by_value("orange") 
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()