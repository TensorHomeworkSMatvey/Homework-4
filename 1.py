a = list(map(float, input("Введите числа через пробел:").split()))
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]: a[j], a[j+1] = a[j+1], a[j]
print('Отсортированный массив методом "пузырька":', ' '.join(map(str, a)))