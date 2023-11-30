


class Queue():
    def __init__(self):
        self.content=[]


    def appendTail(self,item):
        self.content.append(item)

    def deleteHead(self):
      if self.content!=None:
        pop_item=self.content[0]
        self.content.pop(0)
        return pop_item
      else:
          return None




class Stack():
    def __init__(self):
        self.queue1=Queue()
        self.queue2=Queue()

    def push(self,item):
        self.queue1.appendTail(item)


    def pop(self):  #弹出 应为从queue1中从头弹出到queue2中，queue只留最后一个元素，然后弹出该元素,这样交互;

        if self.queue1.content!=[]: #判断方式为是否queue里有元素,因为执行pop后必然只有一个queue有元素。
           n=len(self.queue1.content)
           for i in range(n-1):
               deletehead_item=self.queue1.deleteHead()
               self.queue2.appendTail(deletehead_item)
           pop_item=self.queue1.deleteHead()
           return pop_item
        if self.queue2.content!=[]:
            n = len(self.queue2.content)
            for i in range(n - 1):
                deletehead_item = self.queue2.deleteHead()
                self.queue1.appendTail(deletehead_item)
            pop_item = self.queue2.deleteHead()
            return pop_item


stack=Stack()
stack.push("a")
stack.push("b")
stack.push("c")
print(stack.pop())
print(stack.pop())
stack.push("d")
print(stack.pop())