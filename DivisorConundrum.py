def gcd(a, b):
    if min (a,b)==0:
        return max(a, b)
    else:
        return gcd(b, a%b)
n = int(input())
a = list(map(int, input().split()))
m = max(a)+1
t = [0]*(m)
for i in a:
    t[i] += 1
s = [0]*(m)
for num in range(1, m):
    for j in range(num,m, num):
            s[num] += t[j]
for _ in range(int(input())):
    p,q = map(int, input().split())
    g = gcd(p, q)
    y = p*q//g
    ans = 0
    if p<=m-1:
        ans+=s[p]
    if q<=m-1:
        ans+=s[q]
    if y<= m-1:
        ans-=s[y]
    print(ans)