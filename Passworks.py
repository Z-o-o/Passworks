from PasswordChecker import Checker
from PasswordGenerator import generator
def main():
  while True:
       password = input("Enter your passwaord (hit enter with no text to quit or type \"generate\" to auto-generate a strong password): ")
       if password == '':
           exit(1)
       if password == 'generate':
           print("New Password: " + str(generator(100, 100)) + "\n")
           exit(0)
       checker = Checker(password)
       results = checker.check()
       print(results)
       if(results =="Valid password"):
           pwd_strength = checker.analyze_password()
           print("Your password is: ", pwd_strength)
         
    
if __name__ == '__main__':
    main()