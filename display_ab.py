if __name__ == '__main__':
    
    def append_letter(array, a_count, b_count):
        if len(array) >= 2 and array[-1] == array[-2]:
            # If the last two letters are the same, append the opposite letter
            if array[-1] == 'A' and b_count > 0:
                array.append("B")
                b_count -= 1
            elif a_count > 0:
                array.append("A")
                a_count -= 1
        else:# Prefer to append the letter with more counts remaining
            if a_count > b_count and a_count > 0:
                array.append("A")
                a_count -= 1
            elif b_count > 0:
                array.append("B")
                b_count -= 1
        return a_count, b_count

    def sort_list():
        a_count = int(input("Input number of A : "))
        b_count = int(input("Input number of B : "))
        result = []
        while a_count > 0 or b_count > 0:
            prev_a_count, prev_b_count = a_count, b_count
            a_count, b_count = append_letter(result, a_count, b_count)
            # check stuck in infinite loop
            if a_count == prev_a_count and b_count == prev_b_count:
                 print("error")
                 exit()
        check = result[-3:]
        if len(result) > 3 and len(set(result[-3:])) == 1:
            print("Error")
            exit()
        else:
            result = ''.join(result)
            print("Output :", result)        

sort_list()
