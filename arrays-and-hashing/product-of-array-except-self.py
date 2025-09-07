# Solution 1 Bute Force not efficient 
class Solution1(object):
    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)

        for i, n1 in enumerate(nums):
            prod = 1
            for j, n2 in enumerate(nums):
                if j != i:
                    prod *= n2
            res[i] = prod

        return res


# Solution 2 more efficient
class Solution2(object):
    def productExceptSelf2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(nums)
            
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]        
        
        return res