class Solution:
	
    def ge_than(self, A, B):
        i = 0
        j = 0
        sequences = 0
        sum_sequence = A[0]
        while i<len(A):
            if sum_sequence>=B:
                if i<=j:
                    sequences += (len(A)-j)
                    sum_sequence -= A[i]
                    i += 1
            else:
                if j<len(A)-1:
                    j += 1
                    sum_sequence += A[j]
                else:
                    break
        return sequences
    # @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
	def numRange(self, A, B, C):
        return self.ge_than(A, B)-self.ge_than(A, C+1)