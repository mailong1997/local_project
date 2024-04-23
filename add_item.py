n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

k = int(input())
x = int(input())

def array(a,k,x):
    a.insert(k,x)
    return a
b = array(a, k,x)

for i in range(len(b)):
    print(b[i],end =" ")