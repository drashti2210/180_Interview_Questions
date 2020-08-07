import sys

# Day 3
# 2. Find x^n in log n
# INPUT:-
# n & x
# 1
# 2 3
# OUTPUT:-
# 8

#input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for t in range(int(input())):
    x,n=map(int,input().split())
    #solution 1 
    # iterative solution
    # Time Complexity O(logn)
    if n == 0:
            print(1.0)
    else:
        res = 1.0
        if n < 0: 
            x = 1 / x 
            n = -n
        while n > 0:
            if n % 2 == 1:
                res = res * x
            x *= x
            n//=2
        print(res)

    # solution 2
    # using bitwise operators
    # Time Complexity O(logn)
    if n < 0:
        x = 1 / x
        n = -n
    ans = 1
    while n:
        if n & 1:
            pow *= x
        x *= x
        n >>= 1
    print(ans)

    # solution 3
    # recursive function
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

    