class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class Circularlist:
    def _init_(self):
        self.head=None
        self.temp=None
        self.tail=None
    def create(self):
        size=int(input("Enter the Size of the List:"))
        for i in range(size):
            value=int(input("Enter the Value:"))
            newnode=Node(value)
            if self.head is None:
                self.head=newnode
                self.tail=newnode
            else:
                self.tail.next=newnode
                self.tail=newnode
            self.tail.next=self.head
    def insertfront(self):
        value=int(input("Enter the front Value:"))
        newnode=Node(value)
        newnode.next=self.head
        self.head=newnode
        self.tail.next=self.head
    def insertend(self):
        value=int(input("Enter the  end value:"))
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            self.tail.next=self.head
        else:
            self.tail.next=newnode
            self.tail=newnode
            self.tail.next=self.head
    def insertmid(self):
        data = int(input("Enter the mid value: "))
        newnode = Node(data)
        position = int(input("Enter the position: "))
        if position == 0:
            self.insertfront()
            return
        temp = self.head
        for _ in range(position - 1):
            if temp.next == self.head:
                print("Position is out of bounds")
                return
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode
    def deletefront(self):
         if self.head is None:
            print("List is empty")
            return
         if self.head.next == self.head:
            self.head = None
         else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            self.head = self.head.next
            tail.next = self.head
    def deleteend(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            tail = self.head
            prev = None
            while tail.next != self.head:
                prev = tail
                tail = tail.next
            prev.next = self.head
    def deletemid(self):
          p = int(input("Enter the position delete: "))
          if self.head is None:
            print("List is empty")
            return
          if p == 0:
            self.deletefront()
            return
          tail= self.head
          prev = None
          for _ in range(p):
            if tail.next == self.head:
                print("Position is out of bounds")
                return
            prev = tail
            tail = tail.next
          prev.next = tail.next
    def display(self):
        self.temp=self.head
        while self.temp.next is not self.head:
            print(self.temp.data)
            self.temp=self.temp.next
        print(self.temp.data)
obj=Circularlist()
obj.create()
obj.insertfront()
obj.insertend()
obj.insertmid()
obj.deletefront()
obj.deleteend()
obj.deletemid()
obj.display()
