"""
in recursion 
1. base condition : simple possible input
2. find the relation : think how to solve larger problem with help of smaller problem
3. Generalise
"""
##Q1. sum of upto n 
def sum(n):
    if n == 1:
        return n
    return n + sum(n-1)

##Q2. a**b if b= 0 a**b = 0
# fast sol a**b = a**b/2**2 = a**2**b/2
def power(a,b):
    if b == 1:
        return a
    return power(a*a,b//2) if b%2==0 else a*power(a,b-1)

# Q3. grid nxm total path to__ __ __ __reach n,m from 0,0 can mone down and right
######observations if n =1 |__|__|__|__| only one path alse for m=1
# optimal solution use combinations formula total no of steps in each path s= n-1 + m-1  solution: sCn-1
def path_count(n,m):
    if n==1 or m==1:
        return 1
    return path_count(n-1,m) + path_count(n,m-1)

# # Flood fill theory: let we have to change color from 2 to 4
# let image is = [[1 1 1 2 1 1 1 1],
#                [2 2 1 2 2 1 1 1],
#                [0 2 1 3 2 0 0 1],
#                [2 2 2 1 3 1 2 1]]
# base comdition 1) reach the ends of image 2)pixel is not of same color
def floodfill(arr: list,r: int,c: int,tofill: int,prevfill: int):
    rows= len(arr)
    cols = len(arr[0])
    if r <0 or r>=rows or c<0 or c>=cols:
        return
    if arr[r][c] != prevfill:
        return
    arr[r][c] =tofill
    floodfill(arr, r+1, c, tofill, prevfill)
    floodfill(arr, r , c+ 1, tofill, prevfill)
    floodfill(arr, r- 1, c, tofill, prevfill)
    floodfill(arr, r, c-1, tofill, prevfill)
def swap(s,l,r):
    s = list(s)
    s[l], s[r] = s[r],s[l]
    s = ''.join(s)
    return s

##perutation of a string
st = set()
def permutation(s,l,r):
    if l==r:
        if s not in st:
            st.add(s)
            print(s)
    for i in range(l,r):
        s = swap(s,l,i)
        permutation(s,l+1,r)#resursion
        s = swap(s,l,i)#backtracking
#game theory
#optimal stratergy to win gam
def coin_max(a,l,r):
    if l+1 == r:
        return max(a[l],a[r])
    return max(a[l] +min(coin_max(a,l+2,r),coin_max(a,l+1,r-1)),a[r] +min(coin_max(a,l+1,r-1),coin_max(a,l,r-2)))

if __name__ == '__main__':
    # print(power(2,10))
    # print(path_count(3,4))
    # arr = [ [1, 1, 1, 2, 1, 1, 1, 1],
    #         [2, 2, 2, 2, 2, 1, 1, 1],
    #         [0, 2, 1, 3, 2, 2, 2, 1],
    #         [2, 2, 2, 1, 3, 1, 2, 1]]
    # floodfill(arr,0,3,4,2)
    # print(arr[0])
    # print(arr[1])
    # print(arr[2])
    # print(arr[3])
    # permutation("abcc",0,4)
    a= [1,5,700,2]
    print(coin_max(a,0,len(a)-1))