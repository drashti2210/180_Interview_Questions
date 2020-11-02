import sys

sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')

# Activity Selection
#  Minimum Number of Arrows to Burst Balloons

# Explaination
# There are some spherical balloons spread in two-dimensional space. 
# For each balloon, provided input is the start and end coordinates of the horizontal diameter. 
# Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. 
# The start is always smaller than the end.
# An arrow can be shot up exactly vertically from different points along the x-axis. 
# A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. 
# There is no limit to the number of arrows that can be shot. 
# An arrow once shot keeps traveling up infinitely.
# Given an array points where points[i] = [xstart, xend], 
# return the minimum number of arrows that must be shot to burst all balloons.

# Example
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: One way is to shoot one arrow for example at x = 6 
# (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x: x[1])
        n, count = len(points), 1
        if n == 0: 
            return 0
        curr = points[0]
        
        for i in range(n):
            if curr[1] < points[i][0]:
                count += 1
                curr = points[i]
                
        return count  