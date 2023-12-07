

#m*n列方格  (0,0)出发  不能进入行坐标和列坐标数位之和大于k的格子；问该机器人能够到达多少个格子
#x,y>=0
def cout(x,y):
    #计算位数和
    sum=0
    while(x>=1):
        sum+=x%10
        x=x//10
    while(y>=1):
        sum+=y%10
        y=y//10
    return sum

def movecore(x1,y1,k,list): #准备进入的位置


    check=True
    if check==False:
        return 0
    if x1>=0 and y1>=0 and cout(x1,y1)<=k and (x1,y1) not in list:
        list.append((x1,y1))
        movecore(x1 + 1, y1, k, list)
        movecore(x1 - 1, y1, k, list)
        movecore(x1, y1 + 1, k, list)
        movecore(x1, y1 - 1, k, list)
    else:
        check=False


def movecout(k):
    list=[]
    x1=0
    y1=0
    movecore(x1,y1,k,list)
    return list,len(list)

print(movecout(6))
