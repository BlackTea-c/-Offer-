

#输入n个整数，求出最小的k个数
A=[5,7,3,2,4,1,1,4,2,8,9,1,3,11,44,2,0,-1]


def Partition(A,left,right):


    pivot = A[right]
    tail=left-1
    for i in range(left,right):
        if A[i]<=pivot:
            tail+=1
            A[i],A[tail]=A[tail],A[i]

    A[right],A[tail+1]=A[tail+1],A[right]
    return  tail+1



#方案一:
def FindminK(A,K,left,right):
    #我们同样可以基于Partition解决这个问题

    if left>=right:
        return

    tail=Partition(A,left,right)
    print(tail,A)
    if tail==K-1 or tail==K:
        for i in range(0,K):
            print(A[i])
        return
    if tail>K-1:
        FindminK(A,K,left,tail-1)
    else:
        FindminK(A,K,tail+1,right)



FindminK(A,2,0,len(A)-1)


#解法2  适合处理海量数据


import heapq # heapq 堆来咯

# 创建一个空堆
heap = []

# 插入元素时使用负值,实现最大堆
heapq.heappush(heap, -4)
heapq.heappush(heap, -1)
heapq.heappush(heap, -7)
heapq.heappush(heap, -3)


# 弹出并返回最大元素（取反）
max_element = -heapq.heappop(heap)

def FindminK_heap(A,K):
    heap=[]

    for num in A:
        if len(heap)<K:
            heapq.heappush(heap,-num)
        else:
            max_element=-heapq.heappop(heap)
            if  num<max_element:
                heapq.heappush(heap,-num)
            else:
                heapq.heappush(heap,-max_element)
    print("堆中的元素:", [-i for i in heap])

FindminK_heap(A,5)









