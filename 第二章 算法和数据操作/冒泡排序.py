



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

list=[100,6,5,8,33,7,10,1,12,3,4,4,15,1,2,3,2,5,8,10,100,89,23,55,11,0]

bubblesort(list,len(list)-1)
print(list)
