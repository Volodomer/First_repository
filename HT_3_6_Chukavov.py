#Простим називається число, яке ділиться націло лише на одиницю і на саме себе.
#Число 1 не вважається простим. Напишіть програму, яка знаходить усі прості числа в заданому проміжку, виводить їх на екран,
#а потім на вимогу користувача виводить їхню суму або добуток.

def main():
    upper_level = int(input("Введите верхнюю границу диапазона: "))
    prime_numbers = []
    for i in range(upper_level + 1):
        if is_prime(i):
            prime_numbers.append(i)
    print("Простые числа в данном диапазоне:", prime_numbers)
    menu = input("Выберите (1 или 2) что вы собираетесь сделать с этими числами:\n"
                 "1. Вычислите сумму этих чисел\n2. Вычислите произведение этих чисел\n?> ")
    if menu == "1":
        print("Сумма этих чисел составляет:", sum(prime_numbers))
    elif menu == "2":
        product = 1
        for j in prime_numbers:
            product *= j
        print("Произведение этих чисел составляет:", product)
    else:
        print("Приносим извинения, помочь не может")


def is_prime(number):
    answer = True
    if number < 2:
        answer = False
    elif number == 2:
        answer = True
    else:
        for x in range(2, number):
            if number % x == 0:
                answer = False
    return answer

main()
