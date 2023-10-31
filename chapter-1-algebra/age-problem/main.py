class Solution:

    def solution1(self):
        '''
        How many more years so that son and father have 2 as their age ratio?
        (f+x)/(s+x) = 2, in x years
        f + x = 2s + 2x
        f - 2s = x or x = f - 2s
        f - rs or f - 2s
        '''
        f = 42
        s = 12
        r = 2
        return f - r * s # by that time, son is 30 years old, father is 60 years old



    # def solution2(self):
        

    def run(self):
        print(self.solution1())

        # print(self.solution2())

sol = Solution()
sol.run()

"""
PROBLEMS:
1. A man 42 years old has a son 12. In how many years will the father be twice as old as his son?

"""