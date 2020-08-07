import sys

#Day 4
# 5. Count number of subarrays with given XOR
# INPUT:-
# array
# XOR
# 1
# 4 2 2 6 4
# 6
# OUTPUT:-
# 4

#input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for t in range(int(input())):
    arr=list(map(int,input().split()))
    m=int(input())
    n=len(arr)
    # solution 1 brute force approach - using 2 loops
    # Time Complexity O(n^2) Space Complexity O(1)
    count=0
    for i in range(n):
        xor=0
        for j in range(i,n):
            xor^=arr[j]
            if xor==m:
                count+=1
    print(count)

    # solution 2 using hash map
    # Time Complexity O(n) Space Complexity O(n)

    count = 0
    tempArr =[0 for i in range(n)] 
    dic={} 
    tempArr[0] = arr[0]  
    for i in range(1, n): 
        tempArr[i] = tempArr[i - 1] ^ arr[i] 
    
    for i in range(n): 
        temp = m ^ tempArr[i] 
        if temp in dic: 
            count = count + (dic[temp])
        if (tempArr[i] == m): 
            count += 1
        dic[tempArr[i]] = dic.get(tempArr[i], 0) + 1
    print(count)

