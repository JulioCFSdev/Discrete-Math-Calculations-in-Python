def modular_addition(n_1, n_2, z):
    calculation = (n_1 + n_2)% z
    return calculation


def modular_subtraction(n_1, n_2, z):
    calculation = (n_1 - n_2)% z
    return calculation


def modular_multiplication(n_1, n_2, z):
    calculation = (n_1 * n_2)% z
    return calculation


def modular_inversion(n_1, z):
    inverse = False

    for integer in range(z):
        inverse_count = (n_1*(integer + 1))%z == 1
        if inverse_count:
            print("{} is a modular inverse of {}".format(integer + 1, z))
            inverse = True
            return integer
            
    if inverse == False:
        print("The number {} does not have a modular inverse in {}".format(n_1, z))
        return False

def modular_division(n_1, n_2, z):
    n_2 = modular_inversion(n_2, z)
    calculation = modular_multiplication(n_1, n_2, z)
    return calculation


print("Modular arithmetic  calculator")
print("Discrete Mathematics Subject")

print("press 1 with a modular Addition")
print("press 2 with a modular Multiplication")
print("press 3 with a modular Subtraction")
print("press 4 with a modular Invertion")
print("press 5 with a modular Division")

option = int(input("Which operation do you want to perform?\n"))

if option == 1:
    print("The chosen operation was the modular addition")
    a = int(input("Enter the first value of modular addition: "))
    b = int(input("Enter the second value of modular addition: "))
    n = int(input("Enter the modular comparison value Zn: "))

    result = modular_addition(a, b, n)

    print("{} is the value of the modular addition of {} and {} with Zn equal to {}".format(result, a, b, n))

elif option == 2:
    print("The chosen operation was the modular multiplication")
    a = int(input("Enter the first value of modular multiplication: "))
    b = int(input("Enter the second value of modular multiplication: "))
    n = int(input("Enter the modular comparison value Zn: "))

    result = modular_multiplication(a, b, n)

    print("{} is the value of the modular multiplication of {} and {} with Zn equal to {}".format(calculation, a, b, n))

elif option == 3:
    print("The chosen operation was the modular Subtraction")
    a = int(input("Enter the first value of modular subtraction: "))
    b = int(input("Enter the second value of modular subtraction: "))
    n = int(input("Enter the modular comparison value Zn: "))
    
    result = modular_subtraction(a, b, n)

    print("{} is the value of the modular subtraction of {} and {} with Zn equal to {}".format(result, a, b, n))

elif option == 4:
    print("The chosen operation was the modular inversion")
    a = int(input("Enter the first value of modular inversion: "))
    n = int(input("Enter the modular comparison value Zn: "))
    
    result = modular_inversion(a, n)

    if result == False:         
        print("{} Number has no modular inverse in Z{}".format(a, n))
    else:
        print("{} is the value of the modular inversion of {} with Zn equal to {}".format(result, a, n))

elif option == 5:
    print("The chosen operation was the modular division")
    a = int(input("Enter the first value of modular division: "))
    b = int(input("Enter the second value of modular division: "))
    n = int(input("Enter the modular comparison value Zn: "))
    
    result = modular_division(a, b, n)

    if result == False:         
        pass
    else:
        print("{} is the value of the modular division of {} and {} with Zn equal to {}".format(result, a, b, n))
