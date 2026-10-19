class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        num_dict = {}

        for idx, num in enumerate(nums):
            need = target - num

            if need in num_dict:
                return [num_dict[need], idx]

            else:
                num_dict[num] = idx




sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4],  6))
print(sol.twoSum([3,3],  6))
        