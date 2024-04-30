import math


class Solution():

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

    @staticmethod
    def F9():
        
        def F(nums):
            M = {}
            for i in nums:
                if i in M:
                    del M[i]
                else:
                    M[i] = 1
            return list(M)[0]
        
        # Input
        N = int(input())
        nums = list(map(int, input().split()))
        
        # Function
        natija = F(nums)
        
        # Output
        print(natija)
    
    @staticmethod
    def F10():

        # Algorithm | Algoritm
        # Function | Funksiya
        def F(n: int, nums: list) -> str:

            if sum(nums) >= n:
                return "Yes"
            else:
                return "No"
            
        # Input | Kirish
        N = int(input())
        nums = list(map(int, input().split()))

        # Processing | Ishlov Berish
        natija = F(N, nums)

        # Output | Chiqish
        print(natija)

    @staticmethod
    def F11():

        # Algorithm | Algoritm
        # Function | Funksiya
        def F(nums: list):
            nums.remove(max(nums))
            return max(nums)

        # Input | Kirish
        N = int(input())
        nums = list(map(int, input().split()))

        # Processing | Ishlov Berish
        natija = F(nums)

        # Output | Chiqish
        print(natija)

    def SieveOfEratosthenes(self, n):

        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):

            if (prime[p] == True):

                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1

        rel = []
        for p in range(2, n+1):
            if prime[p]:
                #print(p)
                rel.append(p)
        return rel

    def F12(self):

        # Algorithm | Algoritm
        # Function | Funksiya
        def F(n: int) -> str:
            tub = self.SieveOfEratosthenes(n)
            if len(tub) % 2 == 0:
                return "Bobur"
            else:
                return "Ali"

        # Input | Kirish
        N = int(input())

        # Processing | Ishlov Berish
        natija = F(N)

        # Output | Chiqish
        print(natija)

    @staticmethod
    def F13():

        # Algorithm | Algoritm
        # Function | Funksiya
        def F(N, K):
            
            if N == 0:
                return 1
            return 1 + K
        
        # Input | Kirish
        N, K = tuple(map(int, input().split()))
        
        # Processing | Ishlov Berish
        natija = F(N, K)

        # Output
        print(natija)

    @staticmethod
    def F14():

        # Algorithm | Algoritm
        # Function | Funksiya
        def F(N, K):
            mod = 1_000_000_007
            if N == 0:
                return 1
            return pow(K + 1, N, mod)
    
        # Input | Kirish
        N, K = tuple(map(int, input().split()))
        
        # Processing | Ishlov Berish
        natija = F(N, K)

        # Output
        print(natija)

    def toldiruvchi(self, N: str) -> list[int]:
        
        n_str = N.rjust(12, "0")
        nums = list(map(int, list(n_str)))
        return nums
    
    def F16(self):

        # Function
        def F(nums: list[int]):

            birlik = {
                1: "bir",
                2: "ikki",
                3: "uch",
                4: "to'rt",
                5: "besh",
                6: "olti",
                7: "yetti",
                8: "sakkiz",
                9: "to'qqiz"
            }

            onlik = {
                1: "o'n",
                2: "yigirma",
                3: "o'ttiz",
                4: "qirq",
                5: "ellik",
                6: "oltmish",
                7: "yetmish",
                8: "sakson",
                9: "to'qson"
            }
            
            milliard = nums[:3]
            million = nums[3:6]
            ming = nums[6:9]
            minggacha = nums[9:]

            def f(nums: tuple[int], qosh: str):
                if any(nums):
                    uch = f"{birlik[nums[0]]} yuz" if nums[0] else ""
                    ikki = f"{onlik[nums[1]]}" if nums[1] else ""
                    bir = f"{birlik[nums[2]]}" if nums[2] else ""
                    return " ".join(f"{uch} {ikki} {bir} {qosh}".split())
                else:
                    return ""
                

            a = f(milliard, "milliard")
            b = f(million, "million")
            c = f(ming, "ming")
            d = f(minggacha, "")
            return " ".join(f"{a} {b} {c} {d}".split())

        # Input
        N = input()

        # Processing
        nums = self.toldiruvchi(N)

        # Output
        print(F(nums))
        

def main():
    solution = Solution()
    solution.F16()


if __name__ == "__main__":
    main()
    