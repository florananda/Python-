class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        return '{0:08b}'.format(A).count('1')
