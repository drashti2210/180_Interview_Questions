import sys
#Day-2
#2. Pascal Triangle
#Example
#INPUT:-
# 1st line no of test case-t
# a non-negtive integer
# 2
# 3
# 5
#OUTPUT:-
# Pascal Triangle
# [[1]
# [1, 1]
# [1, 2, 1]]
# [[1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]]

#Input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')
for t in range(int(input())):
    n=int(input())
    ans = [[1]*(i+1) for i in range(n)]
    #print(ans)
    for i in range(n):
        for j in range(1,i):
            ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
    for i in range(n):
        print(ans[i])