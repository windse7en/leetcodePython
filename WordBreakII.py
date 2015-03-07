class Solution:
# @param s, a string
# @param dict, a set of string
# @return a list of strings

# Backtrack:
# 1.divide the string by the length
# 2.when the length is 0 put the string into the list
# TIPS:
# 1.As it's recursion, the string need to be reverse
# 2. i should be to s.lenght + 1
    def wordBreak(self, s, dict):
        result_list = []
        self.helper(s, dict, "", result_list)
        return result_list


    def helper(self, s, d, r, rl):
        if s.__len__() == 0:
            rl.append(r[1:])
            return True
        for i in range(s.__len__()+1):
            if s[0:i] in d:
                print s[0:i]
                self.helper(s[i:], d, r+' '+s[0:i], rl)

test = Solution()
dict = ["cat", "cats", "and", "sand", "dog"]
s = "catsanddog"
print test.wordBreak(s, dict)


