import numpy
if __name__ == "__main__":

    def draw(size):
        for row in range(size):
            for letter in range(size):
                if row == letter or row + letter == size - 1:
                    print("*",end="")
                else:
                    print("_",end="")
            print("\r")

    def odd_draw(num):
        if num % 2 == 0:
            print("Incorrect input ,enter odd number!!")
        else:
            draw(abs(num))

odd_draw(input("Input : "))                