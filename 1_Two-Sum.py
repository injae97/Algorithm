# Brute-Force Search
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target :
                    return [i,j]

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums,target))


# Using Dictionary(Hash-Table)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for idx, value in enumerate(nums):
            remaining = target - nums[idx] # 9 - 2 = 7, 9 - 7 = 2

            if remaining in dic: # dic {2: 0}
                return [dic[remaining], idx] # dic[key] --> value approach
            else:
                dic[value] = idx # value : index

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums,target))


