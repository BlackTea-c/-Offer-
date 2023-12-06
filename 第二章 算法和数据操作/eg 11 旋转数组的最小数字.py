
#把一个数组从开始的若干个元素搬到数组的末尾我们称之为数组的旋转


#输入：一个递增排序数组的一个旋转
#输出：旋转数组的最小元素


#data=[1,2,3,4,5] #原始数组
data1=[5,6,7,1,2] #旋转后的数组
data2=[1,2,3,4,5,6,0,1,1,1]
#意思就是输入data1，利用性质 用最高效的办法找出最小值


#双指针秒了

def find_min(data):
    p1=0
    p2=len(data)-1
    stop=False
    while(p1+1<p2 and stop==False):

        im=(p1+p2)//2
        if(data[im]<data[p1] and data[im]<=data[p2]): #中间的小于左边并且小于等于右边 #则属于右 p2=im.
            p2=im

        if(data[im]>=data[p1] and data[im]>data[p2]):  #中间的大于等于左边且大于右边 #则属于左 p1=im.
            p1=im


        else:#不能确定im到底属于左还是右，此时直接遍历
            min=1000
            for i in range(p1,p2+1):
                if data[i]<=min:
                    min=data[i]
            return min
    return data[p2]

a=find_min(data1)
b=find_min(data2)

print(a,b)