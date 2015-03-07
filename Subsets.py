import copy
class Solution:
# @param S, a list of integer
# @return a list of lists of integer

    # from [], if insertion value is bigger than the last, push into the array and append to the list
    # 1. pay attention to deepcopy method
    # 2. list level problem, 
    def subsets(self, S):
        result_list=[]
        r_fixed_list = []
        for i in S:
            r_fixed_list.append([i])
            result_list.append([i])
        result_list.append([])
        self.helper(S, r_fixed_list, result_list)
        return result_list

    def helper(self, s, r_fixed_list, result_list):
        if r_fixed_list[0].__len__() == s.__len__():
            return
        r_list_new = []
        for i in s:
            for j in r_fixed_list:
                if i > j[-1]:
                    n = copy.deepcopy(j)
                    n.append(i)
                    result_list.append(n)
                    r_list_new.append(n)
        self.helper(s,r_list_new, result_list)


test = Solution()
S = [1,2,3]
print test.subsets(S)
