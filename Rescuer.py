t = int(input())

x1, y1, x2, y2,v1,v2 = input().split()

output=[]
for i in range(0,t):
    t1 = float(y1)/float(v1)
    if(t1<0):
        t1 = -t1

    t2 = float(y2)/float(v2)
    output.append("{:.5f}".format(t1+t2,5))


for i in range(0,t):
    print(output[i])
