def sort_choice(numbers):
    for i in range(len(numbers)-1):
        min = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min]:                   # Метод выбора
                min = j

        m = numbers[i]
        numbers[i] = numbers[min]
        numbers[min] = m

from random import randint
numbers = []
k = int(input('Количество элементов: '))
for i in range(k):
    numbers.append(randint(-100, 100))
print("Список в начале: ", numbers)
sort_choice(numbers)
print("Список после сортировки: ", numbers)

