from PasswordChecker import Checker
def main():
  while True:
       passord = input("Enter your passwaord: ")
       checker = Checker(passord)
       results = checker.check()
       print(results)
         
    
if __name__ == '__main__':
    main()