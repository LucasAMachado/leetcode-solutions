class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:

            # check if the sub array is already sorted
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            # get the mid point
            mid = (l + r) // 2

            # check if the current mid point is a new minimum
            result = min(result, nums[mid])

            # check if the mid point is in the right portion or the left portion
            # and search the sub array that the mid point is not apart of

            # mid is apart of left portion -> search the right portion
            if nums[mid] >= nums[l]:
                l = mid + 1

            # mid is apart of the right sorted portion -> search the left portion
            else:
                r = mid - 1

        return result 