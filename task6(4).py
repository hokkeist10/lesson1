quantity = int(input('Введите количество журавликов кратное 6: '))
if quantity%6 == 0:
    katya = quantity/1.5
    serezha = (quantity - katya)/2
    petya = (quantity - katya)/2
    print(f'Катя сделала {katya} журавликов, Петя сделал {petya} журавликов, Серёжа сделал {serezha} журавликов.')
else:
    print('Введённое число не кратно 6.')
