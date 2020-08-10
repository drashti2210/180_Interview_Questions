import sys

# Grid Unique Paths of m x n
# INPUT:-
# m & n (size of grid) 
# 3 2
# 7 3
# OUTPUT:-
# 3
# 28

m,n=map(int,input().split())
def grid_path(m,n):
    # solution using dynamic programming
    # Time Complexity O(mn)
    
    dp = [[1 for x in range(n)] for x in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1]+dp[i-1][j]
    return(dp[-1][-1])