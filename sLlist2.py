class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self
    
    def print_values(self):
        curr = self.head
        if not curr:
            print('SList is empty!')
            return self
        list = []
        while curr:
            list.append(curr.value)
            curr = curr.next
        print(" -> ".join(list))
        return self
    
    def add_to_back(self, val):
      new_node = SLNode(val)
      if self.head == None:
          self.head = new_node
          return self
      curr = self.head
      while curr.next != None:
          curr = curr.next
      curr.next = new_node
      return self
    
    def remove_from_front(self):
        if self.head == None:
            print("SList is empty! Can't remove!")
            return self
        curr = self.head
        self.head = curr.next
        print("{} is removed".format(curr.value))
        return self
    
    def remove_from_back(self):
        if self.head == None:
            print("SList is empty! Can't remove!")
            return self
        if self.head.next == None:
            print("{} is removed".format(self.head.value))
            self.head = None
            return self
        curr = self.head
        while curr.next.next:
            curr = curr.next
        print("{} is removed".format(curr.next.value))
        curr.next = None
        return self

    def remove_val(self, val):
        if self.head == None:
            print("SList is empty! Can't remove!")
            return self
        if self.head.value == val:
            print('{} is removed.'.format(val))
            self.head = self.head.next
            return self
        curr = self.head
        while curr and curr.next:
            if curr.next.value == val:
                print('{} is removed.'.format(val))
                curr.next = curr.next.next
            curr = curr.next
        return self

    def insert_at(self, val, n):
        new_node = SLNode(val)
        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return self
        curr = self.head
        while curr.next and n > 1:
            curr = curr.next
            n -= 1
        new_node.next = curr.next
        curr.next = new_node
        return self      

# =======================================================
sl = SList()
# sl.remove_val('re')
# sl.add_to_front("Sat").add_to_front("Fri").add_to_front("Thurs").add_to_front("Wed").add_to_front("Tue").add_to_front("Mon").add_to_back("End").remove_from_front().remove_from_back().print_values()
# sl.add_to_front("Fri").add_to_front("Thurs").remove_from_front().remove_from_front().remove_from_front().print_values()
sl.add_to_front("Sat").add_to_front("Fri").add_to_front("Thurs").add_to_front("Wed").add_to_front("Tue").add_to_front("Mon").add_to_back("End").remove_val("Tue").insert_at("INSERT", 7).print_values()