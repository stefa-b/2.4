from random import uniform
n = int(input('введите размер списка: '))
num = [uniform(-5,5) for i in range(n)]
print(*list(map('{:.3f}'.format, num)))
a = float(input('введите нижнюю границу интервала: '))
b = float(input('введите верхнюю границу интервала: '))
s = num[::-1].copy()
f = s.index(next((i for i in s if i > 0), -1)) + 1
res_max = max(num)
print('максимум списка: {:.3f}'.format(res_max))
res_sum = sum(num[:-f])
print('сумма списка: {:.3f}'.format(res_sum))
res = [num[i] for i in range(n) if abs(num[i]) < a or abs(num[i]) > b]
res.extend([0] * (n - len(res)))
print('преобразованный список:')
print(*list(map('{:.3f}'.format, res)))