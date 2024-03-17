import math


class Algorithm:

    def count_divisors(self, n):
        divisor_count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                divisor_count += 1
        return divisor_count


    def count_divisors_optimized(self, n):
        divisor_count = 0
        sqrt_n = math.isqrt(n)
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                divisor_count += 2  # We count both i and n/i
        # If n is a perfect square, we've counted sqrt_n only once.
        if sqrt_n * sqrt_n == n:
            divisor_count -= 1
        return divisor_count


class Solution(Algorithm):

    @staticmethod    
    def F1():

        def F(a, b):
            return a + b
        
        # Input
        a, b = tuple(map(int, input().split()))

        # Funksiya
        natija = F(a, b)

        # Output
        print(natija)
        pass

    @staticmethod
    def F2():

        def F(a, b):
            if a > b:
                return ">"
            elif b > a:
                return "<"
            else:
                return "="
            
        # Input
        a, b = tuple(map(int, input().split()))

        # Function
        natija = F(a, b)

        # Output
        print(natija)

    @staticmethod
    def F3():

        def F(a, b):
            return a + b
        
        # Input
        a = int(input())
        b = int(input())

        # Function
        natija = F(a, b)

        # Output
        print(natija)

    @staticmethod
    def F4():

        def F(a, b):
            return a * b
        
        # Input
        a, b = tuple(map(int, input().split()))

        # Function
        natija = F(a, b)

        # Output
        print(natija)

    def F5(self):

        def F(z: int):
            boluvchilari_soni = self.count_divisors_optimized(z)
            if z > 0:
                if boluvchilari_soni % 2 == 0:
                    return boluvchilari_soni
                return boluvchilari_soni + 1
            elif z < 0:
                return boluvchilari_soni
            else:
                return -1
            
        
        z = int(input())
        natija = F(z)
        print(natija)

if __name__ == "__main__":

    solution = Solution()
    solution.F5()
    pass