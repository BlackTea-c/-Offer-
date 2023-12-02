




#initial pe=0
def insertsort(list):
 pe=0
 while(pe<=len(list)-2):
    ready_to_sort=pe+1
    ready_to_sort_num=list[pe+1]
    i=pe
    while(i>=0):
        if ready_to_sort_num<list[i]:
            tem=list[i]
            list[i]=list[ready_to_sort]
            list[ready_to_sort]=tem
            ready_to_sort=i
        i-=1
    pe+=1

 return list
list=[100,6,5,8,33,7,10,1,12,3,4,4,15,1,2,3,2,5,8,10,100,89,23,55,11,0]

print(insertsort(list))

