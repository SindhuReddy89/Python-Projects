from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        sliding = deque()

        for i in range(len(nums)):
            while sliding and sliding[0] < i - k + 1:
                sliding.popleft()

            while sliding and nums[sliding[-1]] < nums[i]:
                sliding.pop()

            sliding.append(i)

            if i >= k - 1:
                result.append(nums[sliding[0]])

        return result
    print(maxSlidingWindow(1,[1,3,-1,-3,5,3,6,7],3))
