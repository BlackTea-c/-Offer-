#给定一个数组，要求输出数组中重复的数字。(书中要求输出其中一个即可)

#最容易想到的方案就是新建一个数组来记录，而书中提到了一种新的处理方式,其计算复杂度比起前者要小很多

data=[1,0,2,4,5,3,4,5,6,2,1,9,8,7,10,2,5,7,8,1,4,5,6,7,8,7,6,4,5]
#原理是利用哈希表的特性
data_len=len(data)
#假设无重复，则从小到大排序后数字a对应索引a
#若数字a重复,则

def duplicate(data,data_len):
    for i in range(data_len):
        while data[i]!=i:
            if data[i]==data[data[i]]:#找到了重复数
                return data[i] #直接停止了循环
            else:
              #实现a!=index时的交换
              record=data[i]
              data[i]=data[data[i]]
              data[record]=record
#s
print(duplicate(data,data_len))


