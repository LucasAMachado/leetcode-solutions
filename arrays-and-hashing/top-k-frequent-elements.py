from collections import defaultdict

# First solution not very efficient
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#
#         freqMap = defaultdict(int)  # number : freq count in nums
#
#         for num in nums:
#             freqMap[num] += 1
#
#         return [num for num, _ in sorted(freqMap.items(), key=lambda x: x[1], reverse=True)][:k]



class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # use a bucket sort algorithm
        # create a map to count the freq of each number

        # use a nested list where the index is the count of a num and the value is a list of numbers
        # that have that count

        # loop through this count list backwards until we have it being the length of K


        freqMap = {}
        countArr = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)

        for num, count in freqMap.items():
            countArr[count].append(num)

        res = []

        for i in range(len(countArr) - 1, 0, -1):
            for n in countArr[i]:
                res.append(n)

                if len(res) == k:
                    return res

        return res