def test(text, *value, name='Egor'):
    b = 0
    for i in value:
        b += i
    return f'{name}, {text}{b}'


print(test('Ваш суммарный балл за тест: ', 1, 0, 0, 1, 3, 1, 0, 1, 0, name='Степан'))


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(21))
