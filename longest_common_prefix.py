class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        first_string = strs[0]

        for i in strs[1:]:
            while first_string != i[:len(first_string)]:
                first_string = first_string[:-1]

            if not first_string:
                return ""

        return first_string
        