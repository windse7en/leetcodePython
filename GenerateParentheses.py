class Solution:
# @param an integer
# @return a list of string

    def generateParenthesis(self, n):
        #BACKTRACKING: iterate all the situation and output the final result into the list
        re_list = []
        self.helper(re_list, '', 0, 0, 0, n)
        print re_list

    def helper(self, result_list, result_item, deep, left_p, right_p, n):
        if (deep == 2*n):
            result_list.append(result_item)

        if (left_p < n) :
            result_item += '('
            self.helper(result_list, result_item, deep+1, left_p+1, right_p, n)
            # As the item has been added, don't forget to resize the item.
            result_item = result_item[:-1]
        
        if (right_p < left_p) :
            result_item += ')'
            self.helper(result_list, result_item, deep+1, left_p, right_p+1, n)

test = Solution()
test.generateParenthesis(3)
