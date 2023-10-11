
# Дан список, заполненный случайным образом нулями и единицами.
# Найдите самую длинную непрерывную последовательность единиц и определите индексы первого и последнего элементов в ней.
def find_longest_increasing_sequence(numbers):
    longest_sequences = []
    current_sequence = []
    for num in numbers:
         # проверяем current_sequence на пустоту или что наше число больше последнего числа из этого списка
        if not current_sequence or num > current_sequence[-1]:
            current_sequence.append(num)
         # иначе просто добавляем число
        else:
             # проверяем длину current_sequence чтобы был не пустым и не был длины 1
            if len(current_sequence) > 1:
                longest_sequences.append(current_sequence)
            current_sequence = [num]

     # данное условие используем для того если else не сработает
     # (может быть из-за того что самая длинная последовательность равна длине листа)
    if len(current_sequence) > 1:
        longest_sequences.append(current_sequence)

     # находим самую длинную по возрастанию последовательность
    longest_length = max(len(seq) for seq in longest_sequences)
     # находим саму последовательность
    longest_sequences = [seq for seq in longest_sequences if len(seq) == longest_length]

    return longest_length, longest_sequences

# В списке чисел найти самую длинную последовательность, которая упорядочена по возрастанию.
# Если таких последовательностей несколько (с одинаковой максимальной длинной), то найти их все.
# Вывести длину самой длинной упорядоченной по возрастанию последовательности и саму последовательность (или несколько).
def find_longest_continuous_sequence(numbers):
    longest_length = 0
    start_index = 0
    end_index = 0
    current_length = 0
    current_start = 0

    for i, num in enumerate(numbers):
         # если число равно одному, начинаем отсчет от этого элемента и увеличваем длину на единицу
        if num == 1:
            if current_length == 0:
                current_start = i
            current_length += 1
          # иначе сбрасываем счетчик
        else:
             # сравниваем текущую последовательность с самой длинной на данный момент
            if current_length > longest_length:
                longest_length = current_length
                start_index = current_start
                end_index = i - 1
            current_length = 0
     # данное условие используем для того если else не сработает
     # проверку делаем, если вдруг окажеться весь лист будет состоять из одних единиц
    if current_length > longest_length:
        longest_length = current_length
        start_index = current_start
        end_index = len(numbers) - 1

    return longest_length, start_index, end_index

# Дан список чисел, заполненный случайным образом нулями и единицами
numbers = [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0]
numbers_1 = [1, 2, 4, 5, 7, 8, 4, 3, 6, 7, 8, 3, 2, 5, 4, 3, 1, 3, 4, 5, 6, 7, 8, 9, 10, 13, 16, 17]

# Найти самую длинную упорядоченную по возрастанию последовательность
longest_length, longest_sequences = find_longest_increasing_sequence(numbers_1)
print("Длина самой длинной упорядоченной по возрастанию последовательности:", longest_length)
print("Самые длинные последовательности:", longest_sequences)

# Найти самую длинную непрерывную последовательность единиц
longest_length, start_index, end_index = find_longest_continuous_sequence(numbers)
print("Длина самой длинной непрерывной последовательности единиц:", longest_length)
print("Индексы первого и последнего элементов:", start_index, end_index)