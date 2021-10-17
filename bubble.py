def sort_bubble(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                c = numbers[j]
                numbers[j] = numbers[j + 1]       # Метод пузырька
                numbers[j + 1] = c

from random import randint
numbers = []
k = int(input('Количество элементов: '))
for i in range(k):
    numbers.append(randint(-100, 100))
print('Cписок в начале: ', numbers)
sort_bubble(numbers)
print("Список после сортировки: ", numbers)