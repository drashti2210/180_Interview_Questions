import sys
sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')
nums=list(map(int,input().split()))

# find Maximum Consecutive Ones
# Solution 1
# Using Count of 1s
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count=0
        max_count=0
        for i in range(n):
            if nums[i]==1:
                count+=1
                if(max_count<count):
                    max_count=count
            else:
                if count>max_count:
                    max_count=count
                count=0
                
        return max_count


# Solution 2
# Using 2 pointers

        start = 0;
        end = 0;
        n = len(nums);
        ans = 0;
        for i in range(n):
            if nums[i] == 0:
                ans = max(ans, end - start)
                start = i
                if(end <= start):
                    end = start
            else:
                end+=1;
        ans = max(ans, end - start)
        return ans

# Solution 3
# In python only

        b = ''.join(map(str, nums))
        return len(max(b.split('0'), key=len))