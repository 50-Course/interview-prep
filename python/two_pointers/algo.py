from typing import List


def two_pointers(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        # calculate the sum of the two numbers
        s = nums[left] + nums[right]
        if s == target:
            # found a solution? return the two numbers that sum to target
            return [nums[left], nums[right]]
        # incresing left index will increase the sum
        if s < target:
            left += 1
        else:
            # acutally decreasing right index will decrease the sum
            right -= 1
    # base case: no solution
    return [-1, -1]
