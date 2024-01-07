
#8*8国际棋盘摆8个皇后，使其不能相互攻击，请问有多少种摆法？


list=[0,1,2,3,4,5,6,7] #第i行 Queen的列号

Permu=[]
def all_(s,i):
    if i==len(s):
       item = s.copy()  # 创建s的副本并赋值给item  很重要！！！！！！！！！！！！！！！！！！！！！！！！！！！
       Permu.append(item)

    else:
        for j in range(i,len(s)):
            s[j],s[i]=s[i],s[j]
            all_(s,i+1)
            s[j],s[i]=s[i],s[j]
all_(list,0)


#现在check对角线就行了，因为默认了不同行不同列
#只需要(a1,b1),(a2,b2)...  check : a2-a1是否等于b2-b1(注意是左上，右下两方向)  a2-a1==b1-b2

for Queens in Permu:
    check=True
    for i in range(len(Queens)):
        for j in range(len(Queens)):
            if i!=j:
                if i-j==Queens[i]-Queens[j] or j-i==Queens[i]-Queens[j]:
                    check=False

    if check==True:
        print(Queens,'成立')



