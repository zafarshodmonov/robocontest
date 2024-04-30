
class Contest_24_04_2024:

    def A(self):
        
        def F(n):
            N = n - 1
            x = int(((((N + 1) * N) / 2) * 2) + 1)
            return sum(range(x, (x + n * 2), 2))

        # Input | Kirish
        n = int(input())

        # Processing | Ishlov Berish
        natija = F(n)

        # Output | Chiqish
        print(natija)
    

def main():
    contest = Contest_24_04_2024()
    contest.A()


if __name__ == "__main__":
    main()
