def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_diabolic(n):
    if "666" in str(n):
        return True
    return False


def print_diabolic_prime():
    counter = 0
    for i in range(100001):
        if is_prime(i) and is_diabolic(i):
            print(i)
            counter += 1
    print(f"Liczb diabelskich i pierwszych zarazem jest {counter} w 100000")


print_diabolic_prime()
