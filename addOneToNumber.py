class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        string_num = ""
        for i in A:
            st = str(i)
            string_num += st
        string_num = int(string_num)
        string_num += 1
        string_num = str(string_num)
        ls = []
        for i in string_num:
            ls.append(int(i))
        return ls