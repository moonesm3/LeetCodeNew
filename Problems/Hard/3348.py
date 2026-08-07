class Solution:
    def prime_factors(self, t):
        i = 2
        factors = []
        while i * i <= t:
            if t % i:
                i += 1
            else:
                t //= i
                factors.append(i)
        if t > 1:
            factors.append(t)
        return factors

    def distinct(self, factors):
        seen = []
        for factor in factors:
            if factor not in seen:
                seen.append(factor)
        return seen

#Got TLE here based on the solution for the problem 3345.py --> using ChatGPT to solve the problem. --> Brute Force is not working

    def smallestNumber(self, num: str, t: int) -> str:
        factors = self.prime_factors(t)
        for factor in self.distinct(factors):
            if factor not in [2, 3, 5, 7]:
                return "-1"
        
        need = {2: factors.count(2), 3: factors.count(3), 5: factors.count(5), 7: factors.count(7)}
        digit_factors = {1: {}, 2: {2: 1}, 3: {3: 1}, 4: {2: 2},5: {5: 1}, 6: {2: 1, 3: 1}, 7: {7: 1}, 8: {2: 3}, 9: {3: 2}}
        
        def use_digit(needed, digit):
            result = needed.copy()
            for prime, amount in digit_factors[digit].items():
                result[prime] = max(0, result[prime] - amount)
            return result

        def minimum_digits(needed):
            twos = needed[2]
            threes = needed[3]
            fives = needed[5]
            sevens = needed[7]
            count = fives + sevens
            count += twos // 3
            twos %= 3
            count += threes // 2
            threes %= 2

            if twos > 0 and threes > 0:
                count += 1
                twos -= 1
                threes -= 1
            if twos > 0:
                count += 1
            if threes > 0:
                count += 1
            return count

        def make_suffix(needed, length):
            answer = ""
            for position in range(length):
                spaces_left = length - position - 1
                for digit in range(1, 10):
                    new_need = use_digit(needed, digit)
                    if minimum_digits(new_need) <= spaces_left:
                        answer += str(digit)
                        needed = new_need
                        break
            return answer
        
        n = len(num)
        prefix_need = [None] * (n + 1)
        current_need = need.copy()
        prefix_need[0] = current_need.copy()
        first_zero = -1
        for i in range(n):
            digit = int(num[i])
            if digit == 0:
                first_zero = i
                break
            current_need = use_digit(current_need, digit)
            prefix_need[i + 1] = current_need.copy()

        if (first_zero == -1 and minimum_digits(current_need) == 0):
            return num

        if first_zero != -1:
            start = first_zero
        else:
            start = n - 1
        for i in range(start, -1, -1):
            current_need = prefix_need[i].copy()
            current_digit = int(num[i])
            for new_digit in range(max(1, current_digit + 1), 10):
                new_need = use_digit(current_need, new_digit)
                remaining_places = n - i - 1
                if minimum_digits(new_need) <= remaining_places:
                    suffix = make_suffix(new_need, remaining_places)
                    return (num[:i] + str(new_digit) + suffix)


        length = max(n + 1, minimum_digits(need))
        return make_suffix(need.copy(), length)

            
my_solution = Solution() 
print(my_solution.smallestNumber(num = "1234", t = 256))       #Output: 1488
print(my_solution.smallestNumber(num = "12355", t = 50))       #Output: 12355
print(my_solution.smallestNumber(num = "11111", t = 26))      #Output: -1
