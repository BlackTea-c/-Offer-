


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


lists=[6,5,8,7,10,1]
print("排序前的序列为：")
for i in lists:
    print(i,end =" ")
print("\n排序后的序列为：")
for i in quick_sort(lists,0,len(lists)-1):
    print(i,end=" ")