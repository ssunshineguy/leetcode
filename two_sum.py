from typing import List

"""
1. Two Sum
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


class RuntimeOptimizedSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        element_container = dict()
        for i in range(len(nums)):
            element_container[nums[i]] = element_container.get(nums[i], []) + [i, ]

        for k, v in element_container.items():
            if element_container.get(target - k):
                if target - k != k:
                    return [v[0], element_container[target - k][0]]
                elif len(element_container[k]) > 1:
                    return [element_container[k][0], element_container[k][1]]


class MemoryOptimizedSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]


if __name__ == "__main__":
    test = RuntimeOptimizedSolution()
    print(test.twoSum([3, 2, 4], 6))
    print(test.twoSum([3, 3], 6))
    print(test.twoSum([2, 7, 11, 15], 9))

    test = MemoryOptimizedSolution()
    print(test.twoSum([3, 2, 4], 6))
    print(test.twoSum([3, 3], 6))
    print(test.twoSum([2, 7, 11, 15], 9))
