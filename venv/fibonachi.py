#Создайте функцию генератор чисел Фибоначчи

def n_user():
    return int(input('Введите число N: '))

def fibonacci(N):
    fib_list = [0, 1]
    while len(fib_list) < N:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    return fib_list

N = n_user()
fibonacci_sequence = fibonacci(N)
print(fibonacci_sequence)