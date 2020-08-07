import sys

#Day 1
#2. Sort an array of 0’s 1’s 2’s without using extra space or sorting algo 
#Example
# INPUT:-
# 1st line no. of test cases-t
# next t lines input for each test cases
    # 1st line size of array -n 
    # 2nd line elements of array
# 2
# 4
# 1 2 1 0
# 3
# 1 0 2

# OUTPUT:-
# [0, 1, 1, 2]
# [0, 1, 2]

#input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

#inplace solution - without extra space
#just change the positions of zeros and twos
for t in range(int(input())):
    arr=list(map(int,input().split()))
    n=len(arr)
    zeros,twos,ones= 0,n-1,0
    while (ones <= twos):
        if arr[ones] ==0:
            arr[zeros], arr[ones] = arr[ones], arr[zeros]
            zeros +=1
            ones +=1
        elif arr[ones] == 2:
            arr[twos], arr[ones] = arr[ones] , arr[twos]
            twos -=1
        else:
            ones +=1
    print(arr)