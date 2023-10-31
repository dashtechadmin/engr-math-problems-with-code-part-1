class Solution:

    def solution1(self):
        '''
        Calculate for x
        x = (1/2)x + (1/6)x + 15000
        x - (1/2)x - (1/6)x = 15000
        x (1-1/2-1/6) = 15000
        x = 15000 / (1-1/2-1/6)
        x = 45000
        '''
        m = 1/2
        d = 1/6
        s = 15000
        return round(float(s / (1 - m - d)), 2) # 45000



    # def solution2(self):
        

    def run(self):
        print(self.solution1())

        # print(self.solution2())

sol = Solution()
sol.run()

"""
PROBLEMS:
1. A man left 1/2 of hi estate to his wife, 1/6 to his daughter, and the remainder, an amount of $15,000, to his son. How large was the entire estate?

"""