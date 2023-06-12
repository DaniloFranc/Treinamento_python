class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len([num for num in nums if len(str(num)) % 2 == 0])


vet = [555,901,482,1771]

a = Solution().findNumbers(vet)

print(a);