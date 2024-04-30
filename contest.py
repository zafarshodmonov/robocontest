import math


class Contest_20_04_2024():

    def A(self):
        
        # Algorithm | Algoritm
        # Function | Funksiya
        def F(a, b, c) -> str:
            res = ""
            my_map = {
                1: "Ali",
                2: "Vali",
                3: "G'ani"
            }
            katta = self.uchta_son_kattasi(a, b, c)
            if type(katta) == tuple:
                for i in katta:
                    res += my_map[i] + "\n"
            else:
                return my_map[katta]
            return res[:-1]
            

        # Input | Kirish
        n = int(input())
        ali = set()
        vali = set()
        gani = set()
        for i in range(n):
            nums = input().split()
            ali.add(int(nums[0]))
            vali.add(int(nums[1]))
            gani.add(int(nums[2]))

        a = len(ali)
        b = len(vali)
        c = len(gani)

        # Processing | Ishlov Berish
        natija = F(a, b, c)

        # Output | Chiqish
        print(natija)
        
    def B():
        
        def F(s: str):
           pass
        
        # Input | Kirish
        s = input()
        
        # Processing | Ishlov Berish
        natija = F(s)

        # Output | Chiqish
        print(natija)

    @staticmethod
    def E():

        def F(ulkan: str) -> str:
            ulkan_uzunlik = len(ulkan)
            stop = ulkan_uzunlik if (ulkan_uzunlik <= 9) else (9 + ((ulkan_uzunlik - 9) // 2))
            sonlar = set(range(1, stop + 1))
            rel = []
            ulkan += "00"

            def Bk(index, stack, sonlar):
                if not sonlar:
                    rel.append(" ".join(list(map(str, stack))))
                    return
                chap = int(ulkan[index])  
                ong = int(ulkan[index : index + 2])
                if (0 < chap < 10) and (chap in sonlar):
                    #print("chap: ", chap) 
                    stack.append(chap)
                    sonlar.remove(chap)
                    Bk(index + 1, stack, sonlar)
                
                if (9 < ong <= stop) and (ong in sonlar):
                    
                    #print("ong: ", ong)
                    stack.append(ong)
                    sonlar.remove(ong)
                    Bk(index + 2, stack, sonlar)
                return
            
            Bk(0, [], sonlar)
            

             
            return rel

        # Input | Kirish
        ulkan = input() # "4111109876532"
        

        # Processing | Ishlov Berish
        permutatsiya = F(ulkan)

        # Output
        print(permutatsiya)

class Contest_21_04_2024():
    
    @staticmethod
    def A():
        
        # Function | Funksiya
        # Algorithm | Algoritm
        def F(n: int):
            if n == 0:
                return "3"
            e = '271828182845904523536028750'
            res = e[:n + 1]
            tekshiriladigan_raqam = int(e[n + 1])
            if tekshiriladigan_raqam >= 5:
                res = str(int(res) + 1)
            else:
                pass
            return "2." + res[1:]

        # Input | Kirish
        n = int(input())

        # Processing | Ishlov Berish
        result = F(n)

        # Output | Chiqish
        print(result)

    @staticmethod
    def B():

        def F(n):
            if n % 7 == 0:
                return "Yes"
            else:
                return "No"
        
        # Input | Kirish
        n = int(input())
        nums = []
        for _ in range(n):
            nums.append(int(input(), 2))

        # Processing | Ishlov Berish
        nums = list(map(F, nums))

        # Output | Chiqish
        for i in nums:
            print(i)

        
def main():
    contest = Contest_20_04_2024()
    contest.E()


if __name__ == "__main__":
    main()
    