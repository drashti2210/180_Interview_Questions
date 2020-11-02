import sys

#Day-1
#3. Repeat and Missing Number
#Example
#Input: -
# 1st line no. of test cases-t
# next t lines input for each test cases
    #1st line size of array (n)
    #elements of array of size n
# Example
# 2
# 3
# 3 1 3
# 6
# 4 3 6 2 1 1
#OUTPUT:-
#missing,repeat
# 2 3
# 5 1

sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')

for t in range(int(input())):
    #solution 1 - By sorting
    #Time Complexity-O(nlogn) Space Complexity-O(1)
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    miss=repeat=0
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            repeat=arr[i]
            break
    arr.remove(repeat)
    for i in range(n):
        if arr[i]!=i+1:
            miss=i+1
            break
    print(miss,repeat)

    #solution 2 
    #Time Complexity O(n) Space Complexity O(1)
    miss=repeat=0
    for i in range(n): 
        if arr[abs(arr[i])-1] > 0:

            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1] 
        else: 
            repeat=abs(arr[i]) 
              
    for i in range(n): 
        if arr[i]>0: 
            miss=i + 1 
    
    print(miss,repeat)

    # solution 3 Using Hashing
    #Time Complexity: O(n) Space Complexity: O(n)
    dic = {} 
    miss=repeat=0
    for i in arr: 
        if not i in dic: 
            dic[i] = True    
        else: 
            repeat=i 
    for i in range(1, n + 1): 
        if not i in dic: 
            miss=i
    print(miss,repeat)   
