
from abc import ABC, abstractmethod
from typing import List


class Solution(ABC):
    """
    This is a top level abstract class for solutions.
    If someone wants to start practice they should simply utilize
    these interfaces in their module and code the solution in that.
    every abstract method is provided with the leetcode problem links.
    """

    @abstractmethod
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/
        1. Two Sum
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
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

        Constraints:
            2 <= nums.length <= 104
            -109 <= nums[i] <= 109
            -109 <= target <= 109
        Only one valid answer exists.
        :param nums:
        :param target:
        :return:
        """
    @abstractmethod
    def missing_numbers(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/missing-numbers/
        Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

        Example 1:
        Input: nums = [3,0,1]
        Output: 2
        Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

        Example 2:
        Input: nums = [0,1]
        Output: 2
        Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

        Example 3:
        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

        Constraints:
        n == nums.length
        1 <= n <= 104
        0 <= nums[i] <=

        All the numbers of nums are unique.

        Follow up: Could you implement a solution using only O(1)
                   extra space complexity and O(n) runtime complexity?
                 :param nums:  Given an array nums containing n distinct numbers in the range [0, n]
                 :return: return the only number in the range that is missing from the array.
                """

