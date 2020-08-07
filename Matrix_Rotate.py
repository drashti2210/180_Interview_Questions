import sys

# Day 2
# 5. Rotate Matrix
# INPUT:-
# 1st line no of test cases-t
# rows cols
# Matrix
# 1
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# OUTPUT: -
# Rotated matrix
# 3  6  9 
# 2  5  8 
# 1  4  7 

sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')


for t in range(int(input())):
    row,col=map(int,input().split())
    matrix=[]
    # solution for square matrix
    for i in range(row):
        matrix.append(list(map(int,input().split())))
    print(matrix)
    for i in range(row): 
        for j in range(i+1, col): 
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)

    matrix=matrix[::-1]
    print(matrix)
    