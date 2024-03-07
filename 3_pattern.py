import numpy
if __name__ == "__main__":
    
    def odd_draw():
        n = int(input("Input : "))
        if n % 2 == 0:
            print("Incorrect input ,enter odd number!!")
        else:
            draw(abs(n))
            
    def draw(size):
        for row in range(size):
            for letter in range(size):
                if row == letter or row + letter == size - 1:
                    print("*",end="")
                else:
                    print("_",end="")
            print("\r")   

odd_draw()                