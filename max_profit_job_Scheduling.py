import sys

sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')

# Maximum Profit in Job Scheduling
# Explaination
# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
# You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that 
# there are no 2 jobs in the subset with overlapping time range.
# If you choose a job that ends at time X you will be able to start another job that starts at time X.

# Example
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job. 
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs=sorted(zip(startTime,endTime,profit))
        @lru_cache(maxsize=None)
        def dp(i):
            if i>=len(jobs): return 0
            l,r=i+1,len(jobs)-1
            j=len(jobs)
            while l<=r:
                m=(l+r)//2
                if jobs[m][0]<jobs[i][1]:
                    l=m+1
                else:
                    r=m-1
                    j=m
            return max(jobs[i][2]+dp(j),dp(i+1))
        return dp(-1)