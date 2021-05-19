print(['1','2','3']['3','4','5'])
# arr = list(map(int,input().split()))
# stack = []
# k = int(input())
# while k:
#     val = max(arr)

    # k -= 1
arr = list(map(int,input().split(',')))
n = len(arr)
arr.sort()
ans = [None]*n
j =0
for i in range(0,n,2):
    ans[i] = arr[j]
    j +=1
if n%2==1:
    for i in range(0,n,3):
        if ans[i] == None:
            ans[i] = arr[j]
            j +=1
    for i in range(1,n,2):
        if ans[i] == None:
            ans[i] = arr[j]
            j +=1
else:
    for i in range(1,n,4):
        if ans[i] == None:
            ans[i] = arr[j]
            j +=1
    for i in range(0,n,3):
        if ans[i] == None:
            ans[i] = arr[j]
            j +=1
print(ans)
