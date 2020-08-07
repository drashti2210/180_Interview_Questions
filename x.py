import sys
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')
for t in range(int(input())):
    k=int(input())
    arr=list(map(int,input().split()))
    n=len(arr)
    cnt=0
    i=1
    count=0
    while i < n:
        if arr[cnt] < arr[i]:
            cnt=i
            count=1
        else:
            count += 1
        if count == k:
            break
        i += 1
    print(arr[cnt])