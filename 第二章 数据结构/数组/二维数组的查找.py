#一个二维数组，每行按从左到右递增，列按从上到下递增。
import time #计算时间
import numpy as np
#输入这样的二维数组与一个整数，判断数组中是否含有该整数

data=np.array([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])

target_num=10

def find_num1(data,target_num):#常规的遍历 O(n^2)
    judge=False
    for i in data:
        for j in i:
            if j==target_num:
                judge=True
    return judge


def find_num2(data,target_num):#从右上角开始，目标数大于则为下区域，小于则在左区域，每次取区域右上角判断是否等于or大于小于
    while(data[0][-1]!=target_num):  #while条件应该是判断data的行列。 所以我这里停止条件搞得有点复杂。
      if data.shape[0]>1 and data.shape[1]>1:
         if target_num>data[0][-1]:
             data=data[1:]
         else:
             data=data[:,:-1]
      else:
          break
    exist=False
    print(data,data.shape)
    if data.shape[0]>1 and data.shape[1]>1:
        if data[0][-1]==target_num:
            exist=True
    else:
        if data.shape[0]==1:
            for i in data:
                for j in i:
                    if j==target_num:
                        exist=True
        if data.shape[1]==1:
            for i in data:
                if i==target_num:
                    exist=True

    print(exist)


find_num2(data,target_num)
