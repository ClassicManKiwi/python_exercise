if __name__ == '__main__':
    
    def checkPassword(password):
        check = True
        special = "!@#$%^&*()-+?_=,<>/[]|"

        if 7 > len(password) > 31:
            check = False

        if 'password' in password.lower():
            check = False
        
        if not any(char.isdigit() for char in password):
            check = False

        if not any(char.isupper() for char in password):
            check = False

        if not any(char in special for char in password):
            check = False

        return password, check
        
print(checkPassword(input("Input Password :")))