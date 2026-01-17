#Checks if a number is multiple and 3 and of 5
def check_multiple(number: int) -> bool:
    if number %3 == 0 and number % 5 == 0:
        return True
    else:
        return False

#Checks if a password is the secret password of Python123    
def check_password(input_string: str) -> bool:
    if input_string == "Python123":
        return "access granted"
    else:
        return "access denied"
    
#gives the amount of tax that needs to be payed by given tax bracket
def calculate_federal_tax(salary: int) -> int:
    if salary > 95375:
        tax_value = 0.24 * salary
    elif salary > 44725:
        tax_value = 0.22 * salary
    elif salary > 11000:
        tax_value = 0.12 * salary
    elif salary <= 11000 and salary >= 0:
        tax_value = 0.10 * salary
    return tax_value