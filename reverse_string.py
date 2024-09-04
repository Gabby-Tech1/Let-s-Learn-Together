class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        index_left = 0
        index_right = len(s) -1

        while index_left < index_right:
            result = s[index_left]
            s[index_left] = s[index_right]
            s[index_right] = result

            index_left += 1
            index_right -= 1

        
