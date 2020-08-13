n=int(input())
x=input()[:n*2]
y=0
z=0
for i in range(0,2*n+1,2):
    if x[i:i+2]=='rr' or x[i:i+2]=='ss' or x[i:i+2]== 'pp':
        print('drw')
    elif x[i:i+2]=='rp' or x[i:i+2]=='ps' or x[i:i+2]=='sr':
        print('b')
        y=y+1
    elif x[i:i+2]=='rs' or x[i:i+2]=='pr' or x[i:i+2]=='sp':
        print('a')
        z=z+1
if y > z :
    print('b wins')
else :
    print('a wins')
