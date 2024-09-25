class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        position =0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[position] = nums[position],nums[i]
                position += 1

        return nums