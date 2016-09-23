strngLen = int(input())
strng = input()


hcount = strng.count("h")
acount = strng.count("a")
ccount = strng.count("c")
kcount = strng.count("k")
ecount = strng.count("e")
rcount = strng.count("r")
tcount = strng.count("t")

carray = [ccount, kcount, tcount]
earray = [acount, ecount, rcount, hcount]


cktminCount = min(carray)
aerhminCount = min(earray)

print(cktminCount)
print(aerhminCount)
if(cktminCount <= aerhminCount/2):
    print(cktminCount)
else:
    print(int(aerhminCount/2))






    



