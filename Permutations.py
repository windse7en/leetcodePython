import copy
class Solution:
# @param num, a list of integer
# @return a list of lists of integers

    def permute(self, num):
        def swap(li, i, j):
            list = copy.deepcopy(li)
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            return list
        def helper(list, start):
            if start >= len(list):
                return
            for ih in xrange(start, len(list)):
                new_list = swap(list, 0, ih)
                print list
                result_list.append(new_list)
                helper(new_list, ih+1)

        result_list = []
        helper(num, 0)
        return result_list

num = [1,2,3]
test = Solution()
print test.permute(num)



