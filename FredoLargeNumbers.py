arraySize = int(input())
stringArray = input().split()
array = [int(n) for n in stringArray]


nquestions = int(input())

output=[]
diction = {}
for i in range(0,nquestions):
    typ,f = input().split()    
    for j in range(0,arraySize):
        
        if(array[j] not in diction):
            diction[array[j]] = array.count(array[j])              
        
        if(int(typ) == 0 and diction[array[j]]>=int(f)):
            output.append(array[j])
            break
        elif(int(typ) == 1 and diction[array[j]]==int(f)):
            output.append(array[j])
            break
        elif(j == arraySize-1):
            output.append(0)
        

for i in range(0, len(output)):
    print(output[i])
