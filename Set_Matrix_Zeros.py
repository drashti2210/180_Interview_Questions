import sys
#Day-2
#1. Set Matrix zeros
#Example
#INPUT:-
# 1st line no of test case-t
# next t lines
    # 1st line no of rows-m
    # next n lines space separated row elements
# 2
# 3
# 1 1 1
# 1 0 1
# 1 1 1
#OUTPUT:-
# None
# Printing matrix
# [[1, 0, 1]
# [0, 0, 0]
# [1, 0, 1]]
# [[0, 0, 0, 0]
# [0, 4, 5, 0]
# [0, 3, 1, 0]]


#Input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for t in range(int(input())):
    m=int(input())
    matrix=[]
    for i in range(m):
        matrix.append(list(map(int,input().split())))
    if m == 0:
            break
    n = len(matrix[0])
    row_zero = False
    for i in range(m):
        if matrix[i][0] == 0:
            row_zero = True
    col_zero = False
    for j in range(n):
        if matrix[0][j] == 0:
            col_zero = True
                
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
        
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0
                    
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0
        
    if col_zero:
        for j in range(n):
            matrix[0][j] = 0
    if row_zero:
        for i in range(m):
            matrix[i][0] = 0
    for i in range(n):
        print(matrix[i])