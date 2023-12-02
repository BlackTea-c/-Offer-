from random import randint

# 来咯，四大排序算法：插入排序，冒泡排序，归并排序，快速排序



#1.快速排序
list=[100,6,5,8,33,7,10,1,12,3,4,4,15,1,2,3,2,5,8,10,100,89,23,55,11,0]


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


lists=[100,6,5,8,33,7,10,1,12,3,4,4,15,1,2,3,2,5,8,10,100,89,23,55,11,0]
print("排序前的序列为：")
for i in lists:
    print(i,end =" ")
print("\n排序后的序列为：")
for i in quick_sort(lists,0,len(lists)-1):
    print(i,end=" ")



