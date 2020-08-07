import sys

# Day 2
# 5. Best time to sell & buy stocks
# INPUT:-
# 1st line no of test cases-t
# stock price
# 1
# 100 180 260 310 40 535 695
# OUTPUT: -
# maximum profit
# 865

sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for t in range(int(input())):
    # solution 1 Greedy Approach
    # Time Complexity O(n) Space Complexity O(1)
    prices=list(map(int,input().split()))
    n=len(prices)
    buy, ans = float('inf'), 0
    for p in prices:
        buy, ans = min(buy, p), max(ans, p-buy)
    print(ans)
