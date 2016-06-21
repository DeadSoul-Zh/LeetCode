class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(1, num + 1):
            result += result[i - (1<<int(math.log(i,2)))] + 1,
        return result
