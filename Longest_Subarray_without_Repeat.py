import sys

#Day 4
# 6. Longest Subarray without repeating character
# INPUT:-
# string
# 1
# abcbaabcdea
# OUTPUT:-
# 5

#input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for t in range(int(input())):
    s=input()
    n=len(s)
    # solution 1 creating another string
    # Time Complexity O(n) Space Complexity O(n)
    b=""
    max=""
    for c in s:
        if c not in b: 
            b+=c
            if len(max)<len(b):
                max=b
        else:
            b=b[b.index(c)+1:]+c   
    print(len(max))

    # solution 2 using hash map
    # Time Complexity O(n) Space Complexity O(n)
    start = maxLength = 0
    temp = {}
    for i in range(len(s)):
        if s[i] in temp and start <= temp[s[i]]:
            start = temp[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)
        temp[s[i]] = i
    print(maxLength)