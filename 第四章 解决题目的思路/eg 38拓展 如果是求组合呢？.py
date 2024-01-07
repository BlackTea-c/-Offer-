



def all_(s,i):
    if i==len(s):
        print(''.join(s))
    else:
        for j in range(i,len(s)):
            s[j],s[i]=s[i],s[j]
            all_(s,i+1)
            s[j],s[i]=s[i],s[j]

#s='abc'
#all_(list(s),0)

'''更正一下eg 38  这样简单吧'''



#求所有组合 1, 2---n

def find_combinations(s, m):
    if m==0:
        return ['']
    if len(s)==m:
        return [s]

    combination=[]

    for i in range(len(s)):
        first=s[i] #a
        remaining=s[i+1:] #bc

        for combo in find_combinations(remaining,m-1): #bc==> b  f(c,0)=['']
            combination.append(first+combo)
            print(combination)

    return combination


string = "ab"
m = 1

result = find_combinations(string, m)
print(result)
