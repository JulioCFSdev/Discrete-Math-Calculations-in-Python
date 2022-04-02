def prime_numbers(number):
    n_divisors = 0
    for integer in range(1, number + 1):
            if number%integer == 0:
                n_divisors += 1
            if n_divisors == 3:
                return False
            elif integer == number and n_divisors == 2:
                return number


def fibonacci_series(n_series):
    fibo_numbers = []
    fibo_prime_numbers = []
    n_1 = 0
    n_2 = 1
    fibo_numbers.append(n_1)
    fibo_numbers.append(n_2)

    for serie in range(1, n_series - 1):
        n = n_1 + n_2
        n_1 = n_2
        n_2 = n
        fibo_numbers.append(n)

        if prime_numbers(n) == False:
            pass
        else:
            fibo_prime_numbers.append(n)
    
    return fibo_numbers, fibo_prime_numbers



print("Fibonacci Calculator")
series = int(input("Please, Please enter the number of series for the fibonacc equation\n"))
list_fibo = fibonacci_series(series)
print("\n{} are the fibonacci numbers in series {}".format(list_fibo[0], series))
print("\n{} are the fibonacci prime numbers in series {}".format(list_fibo[1], series))


        


