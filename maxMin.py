class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min = A[0]
        max = A[0]
        
        for i in A:
            if i < min:
                min = i
            if i > max:
                max = i
        return max+min