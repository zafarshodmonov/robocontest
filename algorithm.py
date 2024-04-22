class Algorithm:

    def uchta_son_kattasi(self, a, b, c) -> int | tuple:
        """
        Bu algoritmning vazifasi berilgan 3 ta sonning eng kattasini qaytaradi.
        Agar katta sonlar teng bo'lib qolsa hamma katta sonlarni qaytaradi. 
        Agar birinchi son katta bo'lsa 1, ikkinchi son katta bo'lsa 2, uchunchi
        son katta bo'lsa 3 qaytaradi. Agar katta sonlar bir nechta bo'lsa, ularni
        kartej ko'rinishida qaytaradi.
        """
        if a > b:
            if a > c:
                return 1
            elif a < c:
                return 3
            else:
                return (1, 3)
        elif a < b:
            if b > c:
                return 2
            elif b < c:
                return 3
            else:
                return (2, 3)
        else:
            if a > c:
                return (1, 2)
            elif a < c:
                return 3
            else:
                return (1, 2, 3)

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

