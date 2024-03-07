if __name__ == "__main__":
    
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
        
    def fibonacci_seq():
        n = int(input("Input : "))
        output = []
        for i in range(n):
            output.append(fibonacci(i))
        print("Output : ", end="")
        print(*output, sep=", ")

fibonacci_seq()
