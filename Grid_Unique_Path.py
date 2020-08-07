import sys

#Day 3
#5. Grid Unique Paths of m x n
# INPUT:-
# m & n (size of grid) 
# 2
# 3 2
# 7 3
# OUTPUT:-
# 3
# 28

#input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for t in range(int(input())):
    # solution using dynamic programming
    # Time Complexity O(mn)
    m,n=map(int,input().split())
    dp = [[1 for x in range(n)] for x in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1]+dp[i-1][j]
    print(dp[-1][-1])