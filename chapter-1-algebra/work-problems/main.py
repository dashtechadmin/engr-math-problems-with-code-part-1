class Solution:

    def solution1(self):
        '''
        No. of trees?
        Form the equation / relationship of the variables first
        (men1 / trees1) * hours1 = (men2 / trees2) * hours2
        (20 / 30) * 4 = (16 / x) * 6
        '''
        men1 = 20
        trees1 = 30
        hours1= 4
        men2 = men1 - 4 # 16
        hours2 = 6
        return round((men2 * hours2) * (trees1) / (men1 * hours1), 2) # x = 36.0
    
    def solution2(self):
        '''
        No. of hours?
        Form the equation / relationship of the variables first
        (work / hours1) + (work / x) = work / hours_together
        (1 / 5) + (1 / x) = (1 / 3)
        1/3 - 1/5 = 1/x
        '''
        work = 1
        hours1 = 5
        hours_together = 3
        return round((work/hours_together - work/hours1) ** -1, 2) # x = 7.5


    def run(self):
        print(self.solution1())

        print(self.solution2())

sol = Solution()
sol.run()

"""
PROBLEMS:
1. 20 men can cut 30 trees in 4 hours. If 4 men leave the job, how many trees will be cut in 6 hours?

2. Worker A can finish a job in 5 hours. When working at the same time as Worker B, they can finish the job in 3 hours. How long does it take for Worker B to finish the job if he works alone?

"""