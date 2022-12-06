# По заданию
a = {"Red": (255, 0, 0), "Green": (0, 128, 0), "Blue": (0, 0, 255)}
print("Словарь с rgb:", a)
# Или с вводом значений из консоли(Стоп-слово: "")
b, dict_rgb = input().split(), dict()
while b != []: dict_rgb[b[0]], b = tuple(map(float, b[1:])), input().split()
print(dict_rgb)