a=int(input())
l=[int(x) for x in input().split()]
l.sort()
x=l[len(l)//2]
print(x)
