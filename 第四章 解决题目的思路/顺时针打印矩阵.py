

#输入一个矩阵，要求从外向里以顺时针的次序依次打印出每一个数字
import numpy as np

numbers=np.array([[1,2,3,4],[5,6,7,8]])
columns=2
rows=4


def printincircle(numbers,columns,rows,start):
    #只能从左到右打印一行:
    end_y=rows-start-1 #代表圈内有end_y列
    end_x=columns-start-1 #代表圈内有end_x行
    #第一步 左到右
    for i in range(start,end_y+1):
          print(numbers[start][i])
    #第二步,上到下
    if start<end_x:
      for i in range(start+1,end_x+1):
          print(numbers[i][end_y])



   #第三步,右下到左下
    if  start<end_y and start<end_x:
       for i in range(end_y):
           print(numbers[end_x][end_y-1-i])

   #第四步,左下到左上
    if start<end_y and start<end_x-1:
       for i in range(end_x-1):
           print(numbers[end_x-1-i][start])




def printclockwisely(numbers,columns,rows):
    if columns<=0 or rows<=0:
        return
    start=0

    while start*2<columns and start*2<rows:
        printincircle(numbers,columns,rows,start)
        start+=1

printclockwisely(numbers,columns,rows)