import random
x  =  [random.randint(1,100) for x in range (10) ]
print(x)

x = {'a':[10,20,[30,40,50,[70,80],90]],'b':[5]}
# for i in x:
#     print(i)
a = (x.values())
print(a)
for i in a:
    print("this is i",i)
    break
for j in i:
    print("this is j",j)
l = list()
for k in j:
    l.append(k)
print(l[3])
