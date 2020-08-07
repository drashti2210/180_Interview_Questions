import sys

#Day 4
# 2. Longest Consecutive Sequence
# INPUT:-
# array
# 1
# 100 4 200 2 3 1
# OUTPUT:-
# 4

#input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for t in range(int(input())):
    num=list(map(int,input().split()))
    num=set(num)
    # solution using set
    # O(n)
    maxLen=0
    while num:
        n=num.pop()
        i=n+1
        l1=0
        l2=0
        while i in num:
            num.remove(i)
            i+=1
            l1+=1
        i=n-1
        while i in num:
            num.remove(i)
            i-=1
            l2+=1
        maxLen=max(maxLen,l1+l2+1)
    print(maxLen)