class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            # Duplicate Values Pass
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 1):
                # Duplicate Values Pass
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                for k in range(j + 1, len(nums)):
                    # Duplicate Values Pass
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i],nums[j],nums[k]])

        return res


nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))