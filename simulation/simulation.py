class Simulation():
    def findInterval(interval: list, val: int) -> int:
        lo = 0; hi = len(interval) - 1; mid = 0
        while lo < hi:
            mid = (lo + hi) // 2
            
            if lo + 1 == hi:
                return hi if interval[hi] <= val else lo
            
            if interval[mid] < val:
                lo = mid
            elif interval[mid] > val:
                hi = mid
            else:
                return mid
        return lo
    def get(randn, cases, base=100):
        '''
        Input:
        @randn: random numbers, e.g. [09, 06, 51, 62, 83, 61, 59, 20, 82, 68]
        @cases: case with probability: [('case1', 25), ('case2', 75)]
        '''
        cumulative_probability = []
        cumulative_sum = 0
        for case in cases:
            cumulative_probability += [cumulative_sum]
            cumulative_sum += case[1]
        
        return list(map(lambda x: cases[Simulation.findInterval(cumulative_probability, x)][0], randn))
    
    def parseRandN(string: str) -> list:
        '''
        Input:
        @string: string of random numbers, seperated by space, e.g. '09 06 51 62 83 61 59 20 82 68'
        Output:
        @randn: list of random numbers (in int)
        '''
        return list(map(int, string.split(' ')))
    
    def printResult(l: list) -> None:
        '''
        Input:
        @l: list of cases
        '''
        for case in l:
            print(case)
    
if __name__ == '__main__':
    randn = Simulation.parseRandN('09 06 51 62 83 61 59 20 82 68')
    print(Simulation.findInterval([0, 25], 25))
    print(Simulation.get(randn, [('case1', 25), ('case2', 75)]))