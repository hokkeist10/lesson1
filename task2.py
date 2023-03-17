seconds = int(input('Введите время в секундах: '))
hours = round(seconds/3600, 1)
minutes = round(seconds/60, 1)
print(f'Время в формате ч:м:с - {hours} : {minutes} : {seconds}')
