#Follow Sieve of Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        p = 2
        while p * p < n:
            if prime[p]:
                for multiple in range(p * p, n, p):
                    prime[multiple] = False
            p += 1
        return sum(prime)       
    
my_solution = Solution() 
print(my_solution.countPrimes(n = 10))   #Output: 4
print(my_solution.countPrimes(n = 0))   #Output: 0
print(my_solution.countPrimes(n = 1))   #Output: 0
print(my_solution.countPrimes(n = 5))   #Output: 2