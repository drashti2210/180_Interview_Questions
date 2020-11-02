import sys
import collections
sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')

# Minimum Number of Platforms Required for a Railway/Bus Station

# INPUT 
# n= size of arr
# 1 ... n lines cointains (arrival time departure time) 
# OUTPUT 
# no of platforms required
# Example
# 2 -> n
# 1 10
# 5 7

for t in range(int(input())):
    n=int(input())
    arr=[]
    dep=[]
    for i in range(n):
        p,q=map(int,input().split())
        arr.append(p)
        dep.append(p+q)
    arr.sort()
    dep.sort()
    plt = 1
    count = 1
    i = 1
    j = 0
    while (i < n and j < n):
        if (arr[i] <= dep[j]):   
            plt += 1
            i+= 1
        elif (arr[i] > dep[j]):   
            plt -= 1
            j+= 1
        if (plt > count):  
            count = plt
    print(count)