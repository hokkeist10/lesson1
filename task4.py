revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    print(f'Финансовый результат - прибыль. Ее величина: {revenue-costs}')
    k = round((revenue - costs) / revenue, 1)
    print(f'Рентабельность выручки = {k}')
    quantity = int(input('Введите численность сотрудников фирмы: '))
    profit = round((revenue - costs) / quantity, 1)
    print(f'Прибыль фирмы в расчете на одного сотрудника = {profit}')
elif revenue-costs == 0:
    print('Финансовый результат - фирма вышла в ноль.')
else:
    print('Финансовый результат - убыль.')

