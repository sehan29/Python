import string



def checking_white_space(Password):
    if(Password[0] == ' 'or Password[7]==' '):
        return 0
    else:
        return 1


def checking_symboles(symboles):
    number_of_symboles = 0
    for i in symboles:
        if(i in string.punctuation):
            number_of_symboles +=1
    return number_of_symboles

def checking_capital_latter(capitals):
    number_of_capital_latters = 0
    for i in capitals:
        if(i.isupper()):
            number_of_capital_latters +=1
    return number_of_capital_latters         
    
def checking_numbers(digits):
    number_of_ = 0
    for i in digits:
        if(i.isdigit()):
            number_of_ +=1
    return number_of_
    
use = input("Enter Your Password to validate : ")

lenth_of_word = len(use)

if(lenth_of_word == 8):
    white_spc_value = checking_white_space(use)
    if(white_spc_value == 1):
     symbole = checking_symboles(use)
     if(1<=symbole):
        number_of_upper_case= checking_capital_latter(use)
        if(1<=number_of_upper_case):
            number_of_digits = checking_numbers(use)
            if(1<=number_of_digits):
                print("Your Password is Strong")
            else:
                print("Please Check Included digits")
        else:
            print("please Check Included Upper case Characters")
     else:
         print("Please Check Symbols")
    else:
        print("Please Check White Spaces")
     
else:
    print("Lengh is not sufficiantlly")
    
 