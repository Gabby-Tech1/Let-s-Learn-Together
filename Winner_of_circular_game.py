class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        array = []
        winner = 0

        for i in range(1, n+1):
            array.append(i)

        while len(array) > 1:
            winner = (winner + k - 1) 
            winner = winner % len(array)
            array.pop(winner)

        return array[0]
