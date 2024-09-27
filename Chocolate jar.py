N=int(input())
chocolates=list(map(int,input().split()))
total=0
for jar in chocolates:
    if jar%3==0:
        total+=jar//3
    elif jar%3!=0:
        total+=1+jar//3
print(total)
