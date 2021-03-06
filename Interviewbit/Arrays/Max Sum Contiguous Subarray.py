class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maximum = max(A)
        if maximum < 0:
            return maximum
        b = 0
        a = 0
        for i in A:
            a = a + i
            a = max(a,0)
            b = max(b,a)
        return b