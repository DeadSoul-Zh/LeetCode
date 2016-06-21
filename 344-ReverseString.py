class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        l = l.reverse()
        newString = ''.join(l)
        return newString

        # return s[::-1]
