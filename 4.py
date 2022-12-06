'''
Команды
end - конец программы
wrt - вывод содержимого рюкзака
add <название> <вес> - добавление вещи
del <название> - удаление вещи
'''
w = float(input("Введите вес рюкзака:"))
while w < 0:
    print("Вес не может быть отрицательным")
    w = float(input("Введите вес рюкзака:"))
invent, s, real_w = dict(), input("Команда: "), 0
while s != "end":
    if s == "wrt":
        for key, value in invent.items(): print(f'"{key}" с весом {value}; ', end="")
        print(end="\n")
    else:
        s = s.split()
        if s[0] == "add":
            if float(s[2]) < 0: print("Вес не может быть отрицательным")
            elif w >= real_w + float(s[2]):
                invent[s[1]] = float(s[2])
                real_w += float(s[2])
            else: print("Упс! Вещь не влезает в рюкзак")
        if s[0] == "del": invent.pop(s[1])
    s = input("Команда: ")