
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # заданный список
n = 0

primes = []  # список простых чисел
not_primes = []  # список составных чисел
i = 0

for i in range(len(numbers)):
    is_prime = True  # если простое

    n = numbers[i]
    if n < 2:
        print(n, '- не относится ни к простым, ни к составным числам')
        continue
    else:
      m = n ** (1 / 2)  # количество элементов для проверки
    for j in range(2, int(m + 1)):
        if n % j == 0:
            is_prime = False # если составное
            break

    if not (is_prime):
        not_primes.append(n)
    else:
        primes.append(n)
is_prime = True  # признак простого числа
print('Простые числа ', primes)
print('Составные числа', not_primes)

