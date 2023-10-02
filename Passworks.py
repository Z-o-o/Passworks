from PasswordChecker import Checker
def main():
  while True:
       passord = input("Enter your passwaord (or just hit enter with no text to quit): ")
       if passord == '':
           exit(1)
       checker = Checker(passord)
       results = checker.check()
       print(results)
         
    
if __name__ == '__main__':
    main()