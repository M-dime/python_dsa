class Stack():
    def __init__(self):
        self.items = []
    def push (self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items

#[ 1, 3,2, 4]  #  input =  1 3 0 0 1 2  4
#[-1,-1,3,-1]  # 0utpt =  -1 -1 3 3 3 3 -1
def GreatestToLeft(arr):
    stack = Stack()
    ans = []
    for i in arr:
        if stack.is_empty():
            ans.append(-1)
        elif not stack.is_empty() and stack.peek()>i:
            ans.append(stack.peek())
        elif not stack.is_empty() and stack.peek()<=i:
            while  not stack.is_empty() and stack.peek()<=i:
                stack.pop()
            if stack.is_empty():
                ans.append(-1)
            else:
                ans.append(stack.peek())
        stack.push(i)
    return ans

# 2nd loop depend on i and brute force is nested for loop with O(n^2)
#  input =  1 3 0 0 1 2  4
# output =  3 4 1 1 2 4 -1
def GreatestToRight(arr):
    stack = Stack()
    ans = []
    for i in arr[::-1]:
        if stack.is_empty():
            ans.append(-1)
        elif not stack.is_empty() and stack.peek()>i:
            ans.append(stack.peek())
        elif not stack.is_empty() and stack.peek()<=i:
            while  not stack.is_empty() and stack.peek()<=i:
                stack.pop()
            if stack.is_empty():
                ans.append(-1)
            else:
                ans.append(stack.peek())
        stack.push(i)
    return ans[::-1]

#  input =   1 3  0  0 1 2 4
# output =  -1 1 -1 -1 0 1 2
def SmallerToLeft(arr):
    stack = Stack()
    ans = []
    for i in arr:
        if stack.is_empty():
            ans.append(-1)
        elif not stack.is_empty() and stack.peek()<i:
            ans.append(stack.peek())
        elif not stack.is_empty() and stack.peek()>=i:
            while  not stack.is_empty() and stack.peek()>=i:
                stack.pop()
            if stack.is_empty():
                ans.append(-1)
            else:
                ans.append(stack.peek())
        stack.push(i)
    return ans

#Stock spam [100, 80, 60,70, 60, 75, 85]
############[1,1,1,2,1,4,6]
# find cons0cutive smaller or equal
##############output = [1,2,1,1,3,4,7] input=[1, 3, 0, 0, 1, 2, 4]
def StockSpam(arr):
    n = len(arr)
    stack = Stack()
    ans =[]
    for i in range(len(arr)):
        if stack.is_empty():
            ans.append(i-(-1))
        elif not stack.is_empty() and arr[stack.peek()]>arr[i]:
            ans.append(i-stack.peek())
        elif not stack.is_empty() and arr[stack.peek()]<=arr[i]:
            while  not stack.is_empty() and arr[stack.peek()]<=arr[i]:
                stack.pop()
            if stack.is_empty():
                ans.append(i-(-1))
            else:
                ans.append(i-stack.peek())
        stack.push(i)
    return ans

#can we equalize the height
def eqiheight(h1,h2,h3):
    while h1 and h2 and h3:
        s1, s2, s3 =sum(h1), sum(h2), sum(h3)
        ans = min(s1,s2,s3)
        if s1 == s2 == s3:
            return ans
        if s1> ans:
            h1.pop(0)
        if s2>ans:
            h2.pop(0)
        if s3>ans:
            h3.pop(0)
    return -1

def getMax(operations):
    # Write your code here
    stack = []
    for i in operations:
        if i[0] == '1':
            a = i.split()
            stack.append(int(a[1]))
        elif i[0] == '2':
            stack.pop()
        else:
            print(max(stack))
    return stack

#take str as input return bool value
def isBalanced(s):
    stack = []
    hmap = {')': '(', '}': '{', ']': '['}
    for i in s:
        if i in '({[':
            stack.append(i)
            print(stack)
        else:
            k = stack.pop()
            if hmap[i] != k or len(stack) != 0:
                return 'NO'
    return 'YES'

#convert decimal to binary
def converter(n):
    binary = Stack()
    while n>0:
        remainder = n%2
        binary.push(remainder)
        n //=2
    bin_num = ''
    while binary:
        bin_num += str(binary.pop())
    return bin_num

#max area of histogram arr = [6,2,5,4,5,1,6]
#
def areaHistogram(arr):pass
    
if __name__ == '__main__':
    # t = int(input())

    # for t_itr in range(t):
    #     # s = input()
    result = [1, 3, 0, 0, 1, 2, 4]
    print(StockSpam(result))
