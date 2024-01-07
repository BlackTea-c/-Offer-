
#输入字符串,打印出所有排列


string='abcd'
list=set()

def sortstring(string,ps,time_):
    if ps==len(string)-1:
        return
    for i in range(time_):
       str0 = string[:ps]
       str1 = string[ps]
       str2 = string[ps+1:]
       string=str0+str2+str1 #交换
       list.add(string)
       sortstring(string, ps + 1,time_-1)

sortstring(string,0,len(string))
print(len(list))
for str in list:
    print(str)

#如果有重复呢。。。
#如果不用集合来去重呢？
