import random

a, b = {random.randint(1, 100) for i in range(random.randint(10, 30))}, {random.randint(1, 100) for _ in range(random.randint(10, 30))}
print("Первый набор чисел:", ' '.join(map(str, a))), print("Второй набор чисел:", ' '.join(map(str, b)))
print("Входят в оба:", ' '.join(map(str, a&b)))
print("Входят в первое, но не входят во второе:", ' '.join(map(str, a-b)))
print("Входят во второе, но не входят в первое:", ' '.join(map(str, b-a)))
print("Входят в первое или во второе, но не в оба:", ' '.join(map(str, a^b)))