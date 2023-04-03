def LinearSearchStr(str,n,x):
    for i in range(0,n):
        if str[i]==x:
            return i
    return -1

str=['H','E','L','L','O']
n=len(str)
x='L'
res=LinearSearchStr(str,n,x)
if res==-1:
    print(res, "Not found")
else:
    print(res,"Found at index", res)