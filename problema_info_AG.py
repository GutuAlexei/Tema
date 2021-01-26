with open ('input.txt','r') as f:
    x=str(f.readline()) .split(',')
x.sort()
with open ('output.txt', 'w') as f: 
    for a in x:
        f.write(str(a))
        f.write('\n')