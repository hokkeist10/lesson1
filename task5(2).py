number = int(input('Введите трёхзначное число: '))
if number < 1000 and number > 99:
    firstn = number//100
    secondn = (number - 100*firstn)//10
    thirdn = number - 100*firstn - 10*secondn
    count = firstn + secondn + thirdn
    print(f'Сумма цифр данного трёхзначного числа = {count}')
else:
    print('Данное число не является трёхзначным.')
