class Solution:
# @param num, a list of integer
# @return a list of lists of integer
#
# great solution, deep firt traverse, check is in the result or not, from start to the bottom.
# valuelist+[1] will create a new list object.
    def subsetsWithDup(self, S):
        def dft(depth, start, valuelist):
            #res.append(valuelist)
            if valuelist not in res: res.append(valuelist)
            if depth == len(S): return
            for i in xrange(start, len(S)):
                dft(depth+1, i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dft(0,0,[])
        return res

test = Solution()
S = [1,2,3,4]
print test.subsetsWithDup(S)
