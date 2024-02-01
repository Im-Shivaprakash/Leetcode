class Solution:

    def divideArray(self, nums, k: int) :

        len_of_list = len(nums)
        nums.sort()

        new_list = []

        for item in range(0, len_of_list - 2, 3):
            if nums[item] - nums[item + 1] <= k and nums[item + 1] - nums[item + 2] <= k and nums[item + 2] - nums[item] <= k:
                new_list.append([nums[item], nums[item + 1], nums[item + 2]])
            else:
                return []

        return new_list

obj = Solution()
nums = list(map(int,input().split()))
k = int(input())
print(obj.divideArray(nums, k))