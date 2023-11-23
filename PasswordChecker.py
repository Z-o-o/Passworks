import re
class Checker(object):
    def __init__(self, password) -> None:
        self.password =password
        
    def check(self):
        message ={"invalidLength":"Password must be at least 10 charaxters long.",
                  "missingLowercase":"Password is missing a lower case alpha character.",
                  "missingUppercase":"Password is missing an upper case alpha character.",
                  "missingNumeric": "Password is missing a numeric value.",
                  "missingSpecialCharacter":"Password is missing special character.",
                   "validPassword":"Valid password"}
        if len(self.password) < 10:
            self.invalidLength = False
            return message["invalidLength"]
        elif not re.search("[a-z]", self.password):
            return message["missingLowercase"]
        elif not re.search("[A-Z]", self.password):
             return message["missingUppercase"]
        elif not re.search("[0-9]", self.password):
             return message["missingNumeric"]
        elif not re.search("[_@$#]" , self.password):
             return message["missingSpecialCharacter"]
        elif re.search("\s" , self.password):
             return message["invalidLength"]
        else:
             return message["validPassword"]