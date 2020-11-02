import sys

sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')

# N-Queen Problem
# Explaination
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# Example
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0: 
            return [[]]
        
        col = set()
        dig = set()    
        antidig = set() 
        temp = []
        ans = []
        
        def backtrack(row):
            
            if row == n:
                ans.append(temp[:])
                return
            
            for c in range(n):
                if c in col or (row+c) in dig or (row-c) in antidig: 
                    continue
                
                col.add(c)
                dig.add(row+c)
                antidig.add(row-c)
                temp.append('.'*c + 'Q' + '.'*(n-c-1))
                
                backtrack(row+1)
                
                col.remove(c)
                dig.remove(row+c)
                antidig.remove(row-c)
                temp.pop()        
        
        backtrack(0)
        
        return ans