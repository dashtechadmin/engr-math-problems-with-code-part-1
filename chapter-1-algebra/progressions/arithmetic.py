class Solution:

    def solution1(self):
        '''
        Calculate for zth term (25th)
        x, y; where y > x; 
        a, b; where b > a;
        
        Book formula: An = A1 + (n-1)d
        A18 = A1 + 17d; 3 = x + 17y
        A52 = A1 + 51d; 173 = x + 51y
        
        y = x - (a-1) * d - (b-1) * d
        >> y = x - d * (a - 1 - b + 1)
            -> d = (x - y) / (a - b)
        -> A1 = x - 17 * d
        
        x = 3 - 17y
        173 = 3 - 17y + 51y
        170 = 34y
        y = 5; d = 5
        x = -82; A1 = -82
        
        A25 = A1 + (c-1) * d # 38
            -> z = A1 + (c-1) * d
        '''
        x, a = (3, 18)
        y, b = (173, 52)
        c = 25
        d = (x - y) / (a - b)
        A1 = x - (a-1) * d
        return round(A1 + (c-1) * d, 2) # 38


    # def solution2(self):
        

    def run(self):
        print(self.solution1())

        # print(self.solution2())

sol = Solution()
sol.run()

"""
PROBLEMS:
1. The 18th and 52nd terms of an arithmetic progression are 3 and 173, respectively. Find the 25th term.

"""