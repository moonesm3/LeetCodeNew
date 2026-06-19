class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        highest = 0
        for gains in gain:
            altitude += gains
            highest = max(highest, altitude)
        return highest
    

my_solution = Solution()
print(my_solution.largestAltitude(gain = [-5,1,5,0,-7])) #Output: 1
print(my_solution.largestAltitude(gain = [-4,-3,-2,-1,4,3,2])) #Output: 0