import math


# pythonDataStructure.py
# ==== Begin ====
class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def top(self):
        if (not self.isEmpty()):
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items


class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    # Add an item to the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    # Delete an item from the queue
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items
    

class LinkedList:
    pass


class BinaryTreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNode:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class GraphNode:

    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ====  End  ====

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


class Contest_30_04_2024():

    @staticmethod
    def D():

        def F(nums):

            summa = 0
            m = 0
            rel = []
            element = []

            for i in range(3):
                for j in range(3):
                    e = nums[i][j]
                    if m == e:
                        rel.append((i, j))
                        element.append(e)
                    elif m < e:
                        if element:
                            while element[-1] == m:
                                element.pop()
                                rel.pop()
                                if not element:
                                    break
                            
                        else:
                            pass
                        element.append(e)
                        rel.append((i, j))
                        m = e
                        
                    else:
                        pass
                    summa += e
            return summa, rel

        # Input
        nums = []
        for _ in range(3):
            nums.append(list(map(int, input().split())))
        
        # Processing
        natija = F(nums)

        # Output
        print(natija[0])
        for i in natija[1]:
            print(f"{i[0]} {i[1]}")

    @staticmethod
    def E():

        # Algorithm
        def F(ism):
            res = ""
            for i in range(len(ism)):
                res += ism[i:]
                res = res if (i == len(ism) - 1) else res + "\n"
            return res

        # Input
        ism = input()

        # Processing
        result = F(ism)

        # Output
        print(result)


class Contest_10_06_2024():

    def A():
        pass

    def B():
        pass

    def C():
        pass

    def D():
        pass

    def E():
        pass


class Contest_20_06_2024:

    def A(self):

        n = int(input())
        ans = 2 * n - 1
        print(ans)

    def B(self):

        A = int(input())
        B = int(input())
        C = int(input())

        zasum = sum([A, B, C])
        zamax = max(A, B, C)
        
        print(3 * zamax - zasum)

    def C(self):

        n = int(input())

        snake = ""
        camel = ""
        for i in range(n):
            word = input()
            if i == 0:
                snake += word
                camel += word
            else:
                snake += "_" + word
                camel += word.title()
        print(snake)
        print(camel)

    def D(self):

        n = int(input())

        a = {i + 1: e for i, e in enumerate(map(int, input().split()))}
        t = {i + 1: e for i, e in enumerate(map(int, input().split()))}
        d = {i: 0 for i in range(n)}

        for i in range(n):
            for sh, e in t.items():
                if (i + e) in a:

                    if a[i + e] == sh:

                        d[i] += 1
                        
        for i in range(n):
            if i == (n - 1):
                print(d[i], end="")
                break
            print(d[i], end=" ")




def main():
    contest = Contest_20_06_2024()
    contest.D()


if __name__ == "__main__":
    main()
    