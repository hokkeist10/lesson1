revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    print(f'Финансовый результат - прибыль. Ее величина: {revenue-costs}')
else:
    print('Финансовый результат - убыль.')
k = round((revenue-costs)/revenue, 1)
print(f'Рентабельность выручки = {k}')
quantity = int(input('Введите численность сотрудников фирмы: '))
profit = round((revenue-costs)/quantity, 1)
print(f'Прибыль фирмы в расчете на одного сотрудника = {profit}')
