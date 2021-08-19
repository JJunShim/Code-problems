from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     result = None

    #     for a, num_a in enumerate(nums):
    #         for b, num_b in enumerate(nums[a+1:], a+1):
    #             if num_a + num_b == target:
    #                 result = [a, b]

    #     return result

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = dict() # for finding unique index number

        for i, num in enumerate(nums):
            result = target - num

            if result in results:
                return [results.get(result), i]
            else:
                results[num] = i
