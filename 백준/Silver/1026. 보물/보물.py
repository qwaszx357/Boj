n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = []
a.sort()

for i in range(n):
    c.append(a[i] * max(b))
    b.remove(max(b))
print(sum(c))