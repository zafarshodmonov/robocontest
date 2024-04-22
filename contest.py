from algorithm import Algorithm


class Contest_20_04_2024(Algorithm):

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

