n=int(input())
c=n*n
s=0
for i in range(1,n+1):
    d=c%10
    e=c//10
    s+=d
if n==s:
    print('Neon Number')
else:
    print('Not Neon Number')