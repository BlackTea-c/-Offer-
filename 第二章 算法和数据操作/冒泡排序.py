


#这个是我自己编写的:
def bubblesort(list,a):
    if a<1:
        return list
    for i in range(a):
        if list[i]>list[i+1]:
            tem=list[i]
            list[i]=list[i+1]
            list[i+1]=tem
    a-=1
    return bubblesort(list,a)


#这个是参考答案:
def bubbleSort(a, n):
    if n <= 1:
        return
    for i in range(n):
    	# 提前退出冒泡循环的标志位
    	flag = False;
    	for j in range(n-i-1):
    		if a[j] > a[j+1]:
    			# 交换
    			a[j], a[j+1] = a[j+1], a[j]
    			flag = True  # 表示有数据交换
    	if not flag:   # 没有数据交换，提前退出
    		break



list=[100,6,5,8,33,7,10,1,12,3,4,4,15,1,2,3,2,5,8,10,100,89,23,55,11,0]

bubblesort(list,len(list)-1)
print(list)
