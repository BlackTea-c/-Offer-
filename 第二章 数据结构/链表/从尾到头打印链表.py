


#首先得知道什么是链表

#（data + next指针)-->(next)(data1 + next指针)-->...


#首先创建一个链表(这里只写单向链表,其它情况在书的后面几章都会涉及到)


class Node():
    def __init__(self,item):
        self.item=item
        self.next=None

class SingleLinklist():
    def __init__(self):
        self.head=None


    def is_empty(self):
            return self.head is None

    def length(self):
        pointer=self.head.next
        cout=1
        while(pointer!=None):
            pointer=pointer.next
            cout+=1
        return cout

    def add(self,item): #尾部添加元素
        if self.head is None:
            self.head=Node(item)
        else:
            pointer=self.head
            #找到最后一个Node
            while pointer.next is not None:
                pointer=pointer.next
            pointer.next=Node(item)



items=[11,12,13,14,15,16]
singlelinklist=SingleLinklist()
for item in items:
  singlelinklist.add(item)


#从尾到头打印链表


#后进先出思想


#方案一:递归   坏处是当链表非常长的时候就会导致函数调用的层级很深从而导致函数调用栈溢出
head=singlelinklist.head
def PrintListReversely(node):
    if node.next is not None:
        node1=node.next
        PrintListReversely(node1)
    print(node.item)
#PrintListReversely(head)

#方案二:栈   #我感觉python里就是放入列表就行了啊= =

class Stack():
    def __init__(self):
        self.stack=[]#存放元素

    def append(self,node):
        self.stack.append(node)

    def Print_all(self):

        for i in range(1,len(self.stack)+1):
            print(self.stack[-i])
stack=Stack()

items=[11,12,13,14,15,16]
singlelinklist=SingleLinklist()
for item in items:
  singlelinklist.add(item)
  stack.append(item)#添加入栈
stack.Print_all()






