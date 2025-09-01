class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # number : index
        seen = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], index]

            seen[num] = index

        # we do not need this but we can add it
        return []
