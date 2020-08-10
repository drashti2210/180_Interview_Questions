import sys

# Excel Column Number
# INPUT:-
# Column name
# A
# AB
# ZY
# OUTPUT
# 1
# 28
# 701


s=input()
# solution
# reverse the string and add the order of letter in the answer multiplied by 26^index
def excel_col(s):
    ans=0
    n=len(s)
    s=s[::-1]
    for i in range(n):
        ans+=(ord(s[i])-65 + 1)*(26**i)
    return(ans)
        
# from column no to column name
n=int(input())
def excel_col(n):
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
        
