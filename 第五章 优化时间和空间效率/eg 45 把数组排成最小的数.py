

#输入{3,32,321} 得到最小数321 32 3   ;输入的都是正整数数组>0

input_array=[3,32,321]

input_str=[]

for i in input_array:
    input_str.append(str(i))
#最直观的方法就是求全排列



#定义新的大小关系  mn 与 nm
# if mn<nm 则m应该排在n前面   定义此时m<n

def comparemin(m,n):
    #定义出大小并比较m,n的大小，返回小的
    str1=m+n
    str2=n+m

    if int(str1)>int(str2):
        return n
    if int(str1)<int(str2):
        return m
    if int(str1)==int(str2):
        return n

def getmin(input_str):
    if input_str==[]:
        return
    current_min=input_str[0]
    for str in input_str:
        current_min=comparemin(current_min,str)
    return current_min



def getminNum(input):

    minNum=''
    input_str=input
    while True:
        if len(input_str)==1:
            break
        minseg=getmin(input_str)
        minNum+=minseg
        input_str.remove(minseg)
    print(minNum+input_str[0])

getminNum(input_str)








