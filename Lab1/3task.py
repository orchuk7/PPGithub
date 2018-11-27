def proste(a):
    p = True
    for i in range(2 , a):
        if a % i==0:
            p=False
    return p
a=int(input())
b=int(input())
v=True
for i in range(int(a) , int(b)+1):

    if proste(i):
        v=False
        print(i)
if v:
    print("No Simple digits!")