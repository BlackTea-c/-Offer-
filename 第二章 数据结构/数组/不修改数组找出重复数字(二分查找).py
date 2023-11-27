

#不添加辅助数组
#长度为n+1的数组 包含数字1-n
#空间复杂度低
#类似二分查找 ，因为数字是1-n;我们从中间分成两部分 1-m 与m+1-n 计算数字出现的个数；如果1-m次数大于m则在m里，反之则在m+1-n里
data=[2,3,5,4,3,2,6,7]
#该算法无法找出所有的重复数字

split_zone_left=[1,len(data)//2]
split_zone_right=[len(data)//2 + 1,len(data)]

def split_num_comfirm(data,split_zone_left,split_zone_right):
     cout_left=0
     cout_right=0
     for num in data:
        if split_zone_left[0]<=num<=split_zone_left[1]:
            cout_left+=1
        if split_zone_right[1]>=num>=split_zone_right[0]:
            cout_right+=1


     #由数组特征，下式有且仅有一个if能成立
     if cout_left>split_zone_left[1]:
         if split_zone_left[1] - split_zone_left[0] + 1 <3:
             return split_zone_left
         else:
          split_zone_right[1] = split_zone_left[1]
          split_zone_left[1]=(split_zone_left[0]+split_zone_left[1])//2
          split_zone_right[0]=split_zone_left[1]+1





     if cout_right>split_zone_right[1]-split_zone_right[0]+1:
        if split_zone_right[1]-split_zone_right[0]<3:
            return split_zone_right
        else:
         split_zone_left[0]=split_zone_right[0]
         split_zone_left[1]=(split_zone_right[0]+split_zone_right[1])//2
         split_zone_right[0]=split_zone_left[1]+1

split_zone=split_num_comfirm(data,split_zone_left,split_zone_right) #根据需要进行多次split. n//2m<=3 确认m
print(split_zone)
for j in split_zone:
    cout=0
    for i in data:
        if i==j:
            cout=cout+1
    if cout>=2:
        print("duplicate:",j)










