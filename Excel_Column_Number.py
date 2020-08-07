import sys

#Day 3
#1. Excel Column Number
# INPUT:-
# Column name
# 3
# A
# AB
# ZY
# OUTPUT
# 1
# 28
# 701

#input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for t in range(int(input())):
    # solution
    # reverse the string and add the order of letter in the answer multiplied by 26^index
    s=input()
    ans=0
    n=len(s)
    s=s[::-1]
    for i in range(n):
        ans+=(ord(s[i])-65 + 1)*(26**i)
    print(ans)
        
for t in range(int(input())):
    # from column no to column name
    n=int(input())
    s=''
    while n>0:
        rem=n%26
        if rem == 0: 
            s+='Z'
            n//=26
            n-=1
        else: 
            s+= (chr((rem - 1) + ord('A')))
            n//=26
    s=s[::-1]
    print(s)
        
