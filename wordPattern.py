class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        split = s.split()
        pat = []
        for i in pattern:
            pat.append(i)
        if len(pat) != len(split):
            return False
        
        dic = {}
        for i in range(len(pat)):
            if pat[i] not in dic:
                dic[pat[i]] = split[i]
            else:
                if dic[pat[i]] != split[i]:
                    return False
        return True

def main():
    word = Solution()
    sol = word.wordPattern("abba","dog dog dog dog")
    print(sol)
            
if __name__ == "__main__":
    main()
            

            
        