class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        n=len(nums)
        for i in range(n):
            rem=target-nums[i]
            if rem in dict:
                return [dict[rem],i]
            dict[nums[i]]=i
    


nums=[2,7,11,15]
target=9
obj=Solution()
print(obj.twoSum(nums,target))
