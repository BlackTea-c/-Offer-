from random import randint

# 来咯，四大排序算法：插入排序，冒泡排序，归并排序，快速排序



#1.快速排序

#这是我自己写得：
def quick_sort(lists,i,j):
    if i >= j:
        return list
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i]=lists[j]
        while i < j and lists[i] <=pivot:
            i += 1
        lists[j]=lists[i]
    lists[j] = pivot
    quick_sort(lists,low,i-1)
    quick_sort(lists,i+1,high)
    return lists


#参考答案:
def Swap(A, i, j):
    A[i], A[j] = A[j], A[i]
def Partition(A, left, right):  # 划分函数
    pivot = A[right]               # 这里每次都选择最后一个元素作为基准
    tail = left - 1                # tail为小于基准的子数组最后一个元素的索引
    for i in range(left,right):  # 遍历基准以外的其他元素
        if A[i] <= pivot:            # 把小于等于基准的元素放到前一个子数组末尾
            tail += 1
            Swap(A, tail, i)
    # 最后把基准放到前一个子数组的后边，剩下的子数组既是大于基准的子数组
    # 该操作很有可能把后面元素的稳定性打乱，所以快速排序是不稳定的排序算法
    Swap(A, tail + 1, right)
    return tail + 1                    # 返回基准的索引
def QuickSort(A, left, right):
    if left >= right:
        return
    pivot_index = Partition(A, left, right) # 基准的索引
    QuickSort(A, left, pivot_index - 1)
    QuickSort(A, pivot_index + 1, right)
def main():
    A = [5, 2, 9, 4, 7, 6, 1, 3, 8] # 从小到大快速排序
    n = len(A)
    QuickSort(A, 0, n - 1)
    print("快速排序结果：")
    for i in range(n):
        print("%d ", A[i])
    print("\n")





lists=[100,6,5,8,33,7,10,1,12,3,4,4,15,1,2,3,2,5,8,10,100,89,23,55,11,0]
print("排序前的序列为：")
for i in lists:
    print(i,end =" ")
print("\n排序后的序列为：")
for i in quick_sort(lists,0,len(lists)-1):
    print(i,end=" ")



