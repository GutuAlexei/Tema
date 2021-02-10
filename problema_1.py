a=list(int(input('LISTA:')))
print('a' , a[2]+a[3]+a[8])
print('b' , a[1]+a[2]+a[7])
a[0]+=5
a[len(a-1)]+=5
if len(a)%2!=0:
    a[len(a//2)]-=10
else:
    a[len(a//2-1)]-=10
    print('c', a)

