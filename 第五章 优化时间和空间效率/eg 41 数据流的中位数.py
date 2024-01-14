



#还是用堆来实现


import heapq

#尝试自己写一个？

#最大堆吧！
class MAXheap():
    def __init__(self):
        self.heap=[]

    def push(self,item):
        self.heap.append(item)

        self.up(len(self.heap)-1)


    def pop(self):
        max_item=self.heap.pop(0)


        self.down(0)
        return max_item


    def up(self,index):

       while index>0:
           parent_index = (index - 1) // 2  # 父节点的索引=子节点-1 //2
           # 如果新元素大于父节点，交换它们
           if self.heap[index] > self.heap[parent_index]:
               self._swap(index, parent_index)
               index = parent_index
           else:
               break



    def down(self):
        pass





    def _swap(self, i, j):
            # 交换两个节点的值
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]






#输入数据流,假设已经排序
A=[1,3,5,7,8,8,9,15,16,17]

#指针
p1=4
p2=5
#长度
left_max_heap=[]
right_min_heap=[]
for i in A[:p1+1]:
    heapq.heappush(left_max_heap,-i)
for i in A[p2:]:
    heapq.heappush(right_min_heap,i)


def insertAndfindmiddle(A,max_heap,min_heap,insert_item):
    N=len(A)
    #这里可以判断N，然后整合
    #保持左右heap数量;如果总数是偶数那么应该相等;数目之差不能大于1；
    #我们在偶数时插入最小堆，奇数时插入最大堆
    #还要保证左边的最大小于等于右边的最小
    if N%2==0:
        p1=(len(A))//2
        p2=(len(A))//2
    else:
        p1=(len(A)-1)//2
        p2=(len(A)-1)//2 +1





    for item in insert_item:
        if N%2==0:
                heapq.heappush(min_heap,item)
                p2+=1
                # item ***
                if min_heap[0] < -max_heap[0]:
                    heapq.heappush(max_heap, -item)  # item 压入max
                    heapq.heappop(min_heap)  # 删除min的item
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))  # max的最大压入min
        else:
                heapq.heappush(max_heap,-item)
                p1+=1
                if -max_heap[0]>min_heap[0]:
                    #反过来
                    heapq.heappush(min_heap, item)
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))
        N+=1
        print(max_heap,min_heap,p1,p2)


    if N%2==0:
        print((-max_heap[0]+min_heap[0]) / 2)
    else:
        if p1<p2:
            print(min_heap[0])
        if p1>p2:
            print(-max_heap[0])

insert_item=[0,0,0,0,0]
insertAndfindmiddle(A,left_max_heap,right_min_heap,insert_item)

A.extend(insert_item)
import numpy as np

np.array(A)
print(np.median(A))

















