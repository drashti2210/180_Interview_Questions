import sys
sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')

# coin change
# Example
# Output: 3
# Solution
# DP

def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i >= j:
                    dp[i] = min(dp[i], dp[i-j] + 1)

        if dp[amount] == amount+1:
            return -1
        return dp[amount]

# Solution Greedy
# output: included coins
def min_coin(amt): 
    
    coins = [1, 2, 5, 10, 20, 50,100, 500, 1000] 
    n = len(coins) 
    ans = [] 
    i = n - 1
    while(i >= 0):  
        while (amt >= coins[i]): 
            amt -= coins[i] 
            ans.append(coins[i]) 
        i -= 1
    
    for i in range(len(ans)): 
        print(ans[i], end = " ") 