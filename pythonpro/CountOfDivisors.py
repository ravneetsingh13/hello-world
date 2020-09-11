from math import sqrt


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        R = [2] * len(A)
        j = -1
        for e in A:
            i = 2
            j += 1
            sqr = sqrt(e)
            while(i < sqr):
                if(e % i == 0):
                    R[j] += 2
                i += 1
            if(i == sqr):
                R[j] += 1
        return R


s1 = Solution()
res = s1.solve([8, 9, 11, 15, 16, 20, 64, 101, 153, 256])
print(res)
