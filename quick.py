def sort_quick(numbers):
    if len(numbers) <= 1:
        return numbers
    elem = numbers[0]
    left = []
    right = []                                        # Быстрая сортировка
    center = []
    for i in range(len(numbers)):
        if numbers[i] > elem:
            right.append(numbers[i])
        if numbers[i] == elem:
            center.append(numbers[i])
        if numbers[i] < elem:
            left.append(numbers[i])
    print(sort_quick(left) + center + sort_quick(right))
sort_quick([10,3,-4,55,-23,5,89,3,23,12,-45])
print('SORT DONE')
