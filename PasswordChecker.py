import re
class Checker(object):
    def __init__(self, password) -> None:
        self.password =password
        self.message = {"invalidLength":"Password must be at least 10 characters long.",
                  "missingLowercase":"Password is missing a lower case alpha character.",
                  "missingUppercase":"Password is missing an upper case alpha character.",
                  "missingNumeric": "Password is missing a numeric value.",
                  "missingSpecialCharacter":"Password is missing special character.",
                   "validPassword":"Valid password",
                    "StrongPassword":"Strong",
                    "WeakPassword":"Weak",
                    "ModeratePassword":"Moderate Password"}
        
    def check(self):
  
        if len(self.password) < 14:
            self.invalidLength = False
            return self.message["invalidLength"]
        elif not re.search("[a-z]", self.password):
            return self.message["missingLowercase"]
        elif not re.search("[A-Z]", self.password):
             return self.message["missingUppercase"]
        elif not re.search("[0-9]", self.password):
             return self.message["missingNumeric"]
        elif not re.search("[_@$#]" , self.password):
             return self.message["missingSpecialCharacter"]
        elif re.search("\s" , self.password):
             return self.message["invalidLength"]
        else:
             return self.message["validPassword"]
        
    def analyze_password(self):
    # Checking lower alphabet in string 
       hasLower = False
       hasUpper = False
       hasDigit = False
       specialChar = False
       if re.search("[a-z]", self.password):
           hasLower = True
       if re.search("[A-Z]", self.password):
           hasUpper = True
       if  re.search("[0-9]", self.password):
           hasDigit = True
       if re.search("[_@$!#]" , self.password):
           specialChar = True
    # Strength of password 
       if (hasLower and hasUpper and hasDigit and specialChar and len(self.password)  >= 14):
           return self.message["StrongPassword"]
       elif ((hasLower or hasUpper) and specialChar and len(self.password)  >= 14):
           return self.message["ModeratePassword"]
       else:
          return self.message["WeakPassword"]

 