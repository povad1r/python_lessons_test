# n = int(input())
# if n > 0:
#     n = str(n)
#     print(len(n))
n = 123322 
s = str(n)
ln = len(s)
res = 0 

for i in range(ln//2):
    left = s[i]
    right = s[0-i-1]
    if left == right:
        res+=1
if ln % 2:
    print(res+1)
else: 
    print(res)