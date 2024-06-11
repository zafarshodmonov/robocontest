import math


class Solution():

    def toldiruvchi(self, N: str) -> list[int]:
        
        n_str = N.rjust(12, "0")
        nums = list(map(int, list(n_str)))
        return nums
    
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

    def permute(self, nums):
        ans = []
        def B(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            for num in nums:
                if num not in path:
                    path.append(num)
                    B(path)
                    path.pop()
        B([])
        return ans
    
    def F1_processing(self, a, b):
        return a + b 
    
    def F1(self):
        
        # Input
        a, b = tuple(map(int, input().split()))

        # Processing
        natija = self.F1_processing(a, b)

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

    @staticmethod
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

    @staticmethod
    def F15():
        
        # Function | Funksiya
        def F(N, K):
            mod = 1_000_000_007
            if N == 0:
                return 0
            return (pow(K, N, mod) - 1) * pow((K - 1), mod - 2, mod) % mod
    
        # Input | Kirish
        N, K = tuple(map(int, input().split()))
        
        # Processing | Ishlov Berish
        natija = F(N, K)

        # Output
        print(natija)

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

    def F18(self):

        def is_sehr(M: list[int]):
            if (M[0] + M[1] + M[2] == 15) and (M[3] + M[4] + M[5] == 15) \
                and (M[6] + M[7] + M[8] == 15) and (M[0] + M[3] + M[6] == 15) \
                and (M[1] + M[4] + M[7] == 15) and (M[2] + M[5] + M[8] == 15) \
                and (M[0] + M[4] + M[8] == 15) and (M[2] + M[4] + M[6] == 15):
                return True
            return False
        
        def inp():
            rel = []
            for i in range(3):
                nums = list(map(int, input().split()))
                rel = rel + nums
            return rel

        A = inp()
        def tek(A, B):
            s = 0
            for i in range(len(B)):
                s += abs(A[i] - B[i])
            return s
        
        #T1 = list(filter(is_sehr, self.permute(list(range(1,10)))))
        T = [
            [2, 7, 6, 9, 5, 1, 4, 3, 8], 
            [2, 9, 4, 7, 5, 3, 6, 1, 8], 
            [4, 3, 8, 9, 5, 1, 2, 7, 6], 
            [4, 9, 2, 3, 5, 7, 8, 1, 6], 
            [6, 1, 8, 7, 5, 3, 2, 9, 4], 
            [6, 7, 2, 1, 5, 9, 8, 3, 4], 
            [8, 1, 6, 3, 5, 7, 4, 9, 2], 
            [8, 3, 4, 1, 5, 9, 6, 7, 2]]
        
        result = min([tek(A, i) for i in T])
        print(result)

    def F19_(self, N, K):
        return K // N
    
    def F19(self):

        # Input
        N, K = tuple(map(int, input().split()))

        # Processing
        result = self.F19_(N, K)

        # Output
        print(result)

    @staticmethod
    def F20():

        # Algorithm
        def F(N, K):
            return K % N
            
        # Input
        N, K = tuple(map(int, input().split()))

        # Processing
        result = F(N, K)

        # Output
        print(result)

    def ozod_uchun(self):
        def is_sehr(M: list) -> bool:
            if (M[0] + M[1] + M[2] == 14) and (M[1] + M[3] + M[4] == 5) \
                and (M[2] + M[4] + M[5] == 7) and (M[3] + M[6] + M[7] == 13) \
                and (M[4] + M[7] + M[8] == 15) and (M[5] + M[8] + M[9] == 17):
                return True
            return False
        A = self.permute(list(range(10)))
        #T = list(filter(is_sehr, A))
        print("Boshlash")
        for i in A:
            print(i)
        print("Tamom")
        

def main():
    solution = Solution()
    solution.F1()


if __name__ == "__main__":
    main()
    