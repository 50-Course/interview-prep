from typing import List


def strip_dups_in_place(nums: List[int]) -> int:
    """
    Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

    Example:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2]

    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4]

    """

    p1, p2 = 0, 1
    frequency = 0

    # while we still within bounds
    while p1 < len(nums) - 1:
       # and we have our two pointers point to same value 
        # we hit an occurrency, therefore increment the frequency
        while p1 < len(nums) - 1 and nums[p2] == nums[p1]:
            frequency += 1
        else:
            frequency += 1
            p1 = p2
            p2 += 1

    return frequency + 1
    
if __name__ =='__main__':
    input1 = [0,0,1,1,1,2,2,3,3,4]
    input2 =  [1,1,2]
    print(strip_dups_in_place(input2))
    print(strip_dups_in_place(input1))
