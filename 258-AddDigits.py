class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = 0
        while num >= 0:
            n += (num % 10)
            num /= 10
            if num == 0 :
                break;
        if n == 0 :
            return 0
        elif n % 9 != 0:
            return n % 9
        else:
            return 9
