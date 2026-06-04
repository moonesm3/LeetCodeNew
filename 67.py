# 67. Add Binary
class Solution:
        def addBinary(self, a: str, b: str) -> str:
            max_len = max(len(a), len(b))
            a = a.zfill(max_len)
            b = b.zfill(max_len)    
            carry = 0
            result = []      
            for i in range(max_len - 1, -1, -1):
                total = int(a[i]) + int(b[i]) + carry
                carry = total // 2
                result.append(str(total % 2))
            if carry:
                result.append('1')  
            return ''.join(reversed(result))
    
my_solution = Solution()
print(my_solution.addBinary("1010", "1011")) # Output: "10101"
print(my_solution.addBinary("11", "1")) # Output: "100"