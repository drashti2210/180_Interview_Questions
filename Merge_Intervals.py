import sys
#Day-1
#6. Merge overlapping intervals
#Example
#INPUT:-
# 1st line no of test case-t
# next t lines
    # 1st line no of intervals-n
    # next n lines intervals
# 1
# 4
# 6 8 
# 1 9 
# 2 4 
# 4 7
#OUTPUT:-
# All intervals after merging
# [[1, 9]]

#Input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for t in range(int(input())):
    # solution by sorting
    # Time Complexity: O(n) space complexity: O(n)
    n=int(input())
    intervals=[]
    for i in range(n):
        temp=list(map(int,input().split()))
        intervals.append(temp)
    intervals.sort(key=lambda x: x[0])
    ans = []
    for i in intervals:
        if not ans or ans[-1][1] < i[0]:
            ans.append(i)
        else:
            ans[-1][1] = max(ans[-1][1], i[1])
    print(ans)