from algorithm import Algorithm


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

