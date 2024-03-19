import math


class Algorithm:

    def kabisa_yili(self, yil: int) -> bool:
        """
        Bu algoritm 'yil' parametri kabisa yili bo'lsa True, aks holda False
        qaytaradi.

        Parametr:
            yil: int 

        Return:
            bool
        """

        if yil % 400 == 0:
            return True
        else:
            if yil % 4 == 0 and yil % 100 != 0:
                return True
            else:
                return False
        
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
            boluvchilari_soni = self.count_divisors_optimized(abs(z))
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

    def F6(self):
        
        # Input
        yil = int(input())

        # Function
        def F(yil: int) -> str:
            
            if self.kabisa_yili(yil):
                sana = 12
            else:
                sana = 13
            return "{}/09/{:04d}".format(sana, yil)

        # Output
        natija = F(yil)
        print(natija)

    def F7():
        pass

    @staticmethod    
    def F8():

        # Input
        nums = list(map(int, input().split()))

        # Function
        def F(nums: list) -> tuple:
            summa = sum(nums)
            max_ = 0
            min_ = summa

            for i in nums:
                ayirma = summa - i
                min_ = min(min_, ayirma)
                max_ = max(max_, ayirma)
            
            return min_, max_

        # Output
        natija = F(nums)
        print("{} {}".format(*natija))


if __name__ == "__main__":

    solution = Solution()
    solution.F8()
