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

# grid nxm total path to__ __ __ __reach n,m from 0,0 can mone down and right
# observations if n =1 |__|__|__|__| only one path alse for m=1
def path_count(n,m):
    if n==1 or m==1:
        return 1
    return path_count(n-1,m) + path_count(n,m-1)


if __name__ == '__main__':
    print(power(2,10))
    print(path_count(3,4))