n=int(input('LISTA:'))
negative=0
pare=0
nenule=0
div3si5=0
div7911=0
mod3=0
for i in n:
    if i!=0:
        print(negative)
    if i//2==0:
        print (pare)
    if i>0:
        print (nenule)
    if i>0 and i%3==0 and i%5==0:
        print (div3si5)
    if i%7==0 and i%9==0 and i%11==0:
            print (div7911)
    if abs(i)>3:
        print(mod3)