import sys
import collections
sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')

# Permutation in String
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
# In other words, one of the first string's permutations is the substring of the second string.

# Example
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

def checkInclusion(self, s1: str, s2: str) -> bool:
        ns1,ns2 = len(s1), len(s2)

        if ns2 < ns1:
            return False

        s1_ctr = collections.Counter(s1)
        s2_ctr = collections.Counter()

        for i in range(ns2):
            s2_ctr[s2[i]] +=1
            if i >= ns1:
                if s2_ctr[s2[i - ns1]] == 1:
                    del s2_ctr[s2[i - ns1]]
                else:
                    s2_ctr[s2[i - ns1]] -=1
            if s1_ctr == s2_ctr:
                return True
        return False