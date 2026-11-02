
# вариант 13

import random
import math


# равномерное распределение res = min + (max - min)*random
def transmit_one_node_time(average_transmition_time, deviation):
    return ((average_transmition_time - deviation) + 2 * deviation * random.random())


# Генерация экспоненциального времени исправления ошибки
def calculate_fixing_time():
    return -math.log(1 - random.random())


# расчет количества ошибок, вылезших между узлами
def calculate_errors_number(p0, p1):
    errors = random.random()

    if errors < p0:
        return 0
    elif errors < p0 + p1:
        return 1
    else:
        return 2



# моделирование процесса
def modelling(p0, p1):
    transmition_time = 0

    for blok in range(1000):

        #из А в Х
        while True:
            transmition_time += transmit_one_node_time(5, 2)
            curr_error_number = calculate_errors_number(p0, p1)

            if curr_error_number == 0:
                break
            elif curr_error_number == 1:
                transmition_time += calculate_fixing_time()
                break

        #из Х в В
        while True:
            transmition_time += transmit_one_node_time(6, 2)
            curr_error_number = calculate_errors_number(p0, p1)

            if curr_error_number == 0:
                break
            elif curr_error_number == 1:
                transmition_time += calculate_fixing_time()
                break

    return transmition_time



# вероятность отсутствия ошибок
p0 = 0.95
# вероятность одной ошибки
p1 = 0.03
#  вероятность двух и более ошибок
p2 = 0.02
repeats_number = 100
# итоговое время
accumulated_time = 0

for i in range(repeats_number):
    curr_time = modelling(p0, p1)
    accumulated_time += curr_time

average_time = accumulated_time / repeats_number

print("Среднее время передачи 1000 блоков: ", average_time)
print("Среднее время передачи одного блока:", average_time / 1000)
