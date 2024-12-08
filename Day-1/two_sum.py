from typing import List

from solution_utils import utils

class Day1(utils.Solution):

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums) # storing length of nums
        l= -1 # left side of the window
        while True: #looping through the comparision steps
            l +=1
            r = n -1
            while l != r: # comparison loop
                if nums[l] + nums[r] == target:
                    return [l, r]
                else:
                    r -=1
    def missing_numbers(self, nums: List[int]) -> int:
        missing_number = 0
        new_list = [i for i in range(0, max(nums)+1)]
        print(new_list)
        if sorted(nums) == new_list:
            return max(nums) + 1
        for i in nums + new_list:
            missing_number ^= i
        return missing_number


if __name__ == '__main__':
    solution = Day1()
    