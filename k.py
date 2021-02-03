import sys
maxint = sys.maxsize
a=1


while(a<maxint):    
    b=a
    s=0
    while b!=0:
        n=b%10 
        k=1
        for i in range(1,n+1):
            k=k*i
        s=s+k
        b=b//10
    if s==a:
        print('Numerele egale cu suma factoriala' , a)
    a=a+1

