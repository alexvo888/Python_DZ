def sum_digits(a):
    b = 0
    while a != 0:
        b += a % 10
        a //= 10
    return b


numbers = [i ** 3 for i in range(1, 1001, 2)]

my_sum_1 = sum(filter(lambda num: sum_digits(num) % 7 == 0, numbers))
my_sum_2 = sum(filter(lambda num: sum_digits(num + 17) % 7 == 0, numbers))

print("Сумма чисел, которые нацело делится на 7:", my_sum_1)
print("Сумма эелементов списка + 17, которые нацело делится на 7:", my_sum_2)
