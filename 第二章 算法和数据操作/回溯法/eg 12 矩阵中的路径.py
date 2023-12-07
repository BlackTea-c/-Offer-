import numpy as np
import random as rd



M=np.array([['a','b','t','g'],['c','f','c','s'],['j','d','e','h']])

str='bbb'



#书上让随机找，但是我感觉。。直接遍历找到第一个字符为先比较好；哦我懂了，任选一个是吧，是指的人工任选哈哈，小丑原来是我啊，直接(0，0)谢谢
def hasPathCore(matrix,rows,cols,row,col,path,pathlength,markmatrix):
    # 说明已经找到该路径，可以返回True
    if len(str) == pathlength:
        return True

    hasPath = False
    if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row][col] == path[pathlength] and not markmatrix[row][col]:
        pathlength += 1
        markmatrix[row][col] = True
        # 进行该值上下左右的递归
        hasPath = hasPathCore(matrix, rows, cols, row - 1, col, path, pathlength, markmatrix) \
                  or hasPathCore(matrix, rows, cols, row, col - 1, path, pathlength, markmatrix) \
                  or hasPathCore(matrix, rows, cols, row + 1, col, path, pathlength, markmatrix) \
                  or hasPathCore(matrix, rows, cols, row, col + 1, path, pathlength, markmatrix)

        # 对标记矩阵进行布尔值标记，如果当前层的下一层都没有我们要的，那么就要退回到上一层，这个时候pathlength要减1
        if not hasPath:
            pathlength -= 1
            markmatrix[row][col] = False
        return hasPath


def haspath(str,M):
    m,n=M.shape
    M_visited=np.zeros((m,n)) #标识路径是否已经进入了格子 0没 1有
    pathLength=0
    for i in range(m):
        for j in range(n):
            if(hasPathCore(M,m,n,i,j,str,pathLength,M_visited)):
                return True
    return False



print(haspath(str,M))


