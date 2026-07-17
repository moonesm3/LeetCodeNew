def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        primes = []
        for number in range(left, right + 1):
            if isPrime(number):
                primes.append(number)

        if len(primes) < 2:
            return [-1, -1]

        best_pair = [primes[0], primes[1]]
        minimum_distance = primes[1] - primes[0]
        for j in range(1, len(primes)):
            distance = primes[j] - primes[j - 1]
            if distance < minimum_distance:
                minimum_distance = distance
                best_pair = [primes[j - 1], primes[j]]
        return best_pair
               
my_solution = Solution()
print(my_solution.closestPrimes(left = 10, right = 19))   #Output: [11,13]
print(my_solution.closestPrimes(left = 4, right = 6))   #Output: [-1,-1]