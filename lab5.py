# F(1) = 1, F(n) = F(n–1) * (3*n - 2), при n > 1


import time
import matplotlib.pyplot as plt
try:
    # проверка числа на соответсвие условию задания
    n = int(input("Введите число n > 1: "))
    while n <= 2:
        n = int(input("Введите число n > 1: "))
except ValueError:
    print("Ввёденное вами значение n не является числом."
          " Пожалуйста, перезапустите программу и введите корректное значение ")


def F(n):
    if n <= 1:
        return 1
    else:
        return F(n - 1) * (3 * n - 2)


def Iteratively(n):
    if n == 1:
        return 1
    else:
        a = 1
        for i in range(1, n + 1):
            c = a * (3 * i - 2)
            a = c
        return c




# подсчёт времени для рекурсии
start_time = time.time()
f_rec = F(n)
end_time = time.time()
rec_time = end_time - start_time

# подсчёт времени для итерации
start_time = time.time()
f_iter = Iteratively(n)
end_time = time.time()
iter_time = end_time - start_time


#вывод времени
print("F({}) = {} (рекурсивно в {:.6f} секунд)".format(n, f_rec, rec_time))
print("F({}) = {} (итеративно в {:.6f} секунд)".format(n, f_iter, iter_time))


rec_times = []
rec_values = []
iter_times = []
iter_values = []
n_values = list(range(1, n + 1, +1))

for n in n_values:
    '''
    start = time.time()
    rec_values.append(F(n))
    end = time.time()
    rec_times.append(end - start)
'''
    start = time.time()
    iter_values.append(Iteratively(n))
    end = time.time()
    iter_times.append(end - start)


# таблица
table = []
for i, n in enumerate(n_values):
    table.append([n, rec_times[i], iter_times[i], rec_values[i], iter_values[i]])
print("{:<10}|{:<22}|{:<22}|{:<25}|{:<30}".format("n", "Время выполнения рекурсии (с)","Время выполнения итерации (с)","Значение рекурсии", "Значение итерации"))

print('-' * 160)
for j in table:
    print("{:<10}|{:<22}|{:<22}|{:<25}|{:<30}".format(j[0], j[1], j[2], j[3], j[4]))


# графики
plt.plot(n_values, rec_times, label="Рекурсия")
plt.plot(n_values, iter_times, label="Итерация")
plt.xlabel("n")
plt.ylabel("Время (с)")
plt.title("Сравнение рекурсивного и итерационного подхода")
plt.legend()
plt.show()

plt.plot(n_values, iter_times, label="Итерация")
plt.xlabel("n")
plt.ylabel("Время (с)")
plt.title("Итерация")
plt.legend()
plt.show()

print("\nРабота программы завершена.\n")

