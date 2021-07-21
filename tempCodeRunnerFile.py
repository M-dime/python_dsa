# for t in range(1,int(input())+1):
#     n, q = list(map(int,input().split()))
#     arr = list(map(int,input().split()))
#     summ=0
#     for i in range(q):
#         query = input().split()
#         if query[0]=='U':
#             arr[int(query[1])-1] = int(query[2])
#             # print(arr)
#         else:
#             l = int(query[1])
#             r = int(query[2])
#             # print(l, r)
#             for j in range(r-l+1):
#                 q = ((-1)**j)*arr[l+j-1]*(j+1)
#                 # print(q)
#                 summ +=q
#     print(f"Case #{t}: {summ}")

# for t in range(1,int(input())+1):
#     n , k = list(map(int,input().split()))
#     arr = input()
#     need= ""
#     for i in range(k):
#         need += str(k-i)+' '
#     need = need.rstrip()
#     ans =arr.count(need)
#     print(ans)
#
#
# for t in range(1,int(input())+1):
#     g = int(input())
#     count = 0
#     x = int((g*2)**0.5)
#     for i in range(0,x):
#         if (g-(i*(i+1)//2))%(i+1) == 0:
#             count += 1
#     print(count)

# for t in range(1,int(input())+1):
    # n ,k = list(map(int,input().split()))
    # s = input()
    # alpha = "abcdefghijklmnopqrstuvwxyz"
    # dp =[None]*n
    # dp[n-1] = alpha.index(s[n-1])+1
    # for i in range(n-2,-1,-1):
    #     # print(i)
    #     dp[i] = min(dp[i+1],alpha.index(s[i])+1)
    # print(dp)
    # ans = 1
    # if n%2 == 0:
    #     for i in range(n//2):
    #        ans *= dp[i]
    # else:
    #     for i in range(n//2+1):
    #         ans *= dp[i]
#     print(f"Case #{t}: {ans}")
# 3
# 5 2 2 2 2 2 2 2 2 2 2 2
# 5 2 2 2 2 2 2 3 2 2 2 2
# 9 4 2 2 2 2 3 2 2 2 2 2
# 1 2
# 9 225 7283 37 37208 8192 828 82 938 1736 309 939

# cook your dish here
# from math import ceil
#
# for _ in range(int(input())):
#     arr = list(map(int, input().split()))
#     g = arr.pop(0)
#     p = arr.pop(0)
#     i = 10 - g
#     summ = sum(arr[:i])
#     minn = ceil((summ+1)/ p)
#     maxx = ceil((summ+arr[i]) / p)
# #     print(minn, maxx)
# 
# 
# def change(a: list, p: list):
#     print(a)
#     print(p)
#     b = [None] * len(a)
#     for i in range(len(a)):
#         b[i] = a[p[i]]
#     return b
# 
# 
# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     p = list(map(int, input().split()))
#     q = int(input())
#     for i in range(q):
#         query = list(map(int, input().split()))
#         print(query)
#         if query[0] == 1:
#             a = change(a, p)
#             print(a)
#         if query[0] == 2:
#             a[query[2]], a[query[2]] = a[query[2]], a[query[1]]
#         if query[0] == 3:
#             print(a[query[1]])