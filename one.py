#a = 5
#b = 4
#print(a, b)


#num = (input('Введите число: '))
#numb = (input('Введите другое число: '))
#print(f'Вы ввели {num}, {numb}')
#c = input('Введите ваше имя: ')
#print(c,', рад знакомству!')



#t = int(input('Введите секунды:'))
#hours = t//3600
#hours_r = (hours) if hours > 10 else ('0' + str(hours))
#minute = (t % 3600)//60
#minute_r = (minute) if minute > 10 else ('0' + str(minute))
#second = (t % 3600) % 60
#second_r = (second) if second > 10 else ('0' + str(second))
#if hours > 24:
#    print('Количество полученных часов превышает количество часов в сутка, скоректируйте ввод.')
#else:
#    print(f'Московское время: {hours_r}:{minute_r}:{second_r}')



#n = input('Введите число: ')
#nn = int(n + n)
#nnn = int(n + n + n)
#n = int(n)
#result = n + nn + nnn
#print(result)



#n = int(input('Write a number: '))
#max = n % 10
#while True:
#    n = n // 10
#    if n % 10 > max:
#        max = n % 10
#    elif n > 9:
#        continue
#    else:
#        print(f'Максимальное число: {max}')
#        break





#prib = int(input('Введите данные по выручке: '))
#izd = int(input('Введите данные по рассходу: '))

#profit = prib - izd
#if profit < 0:
#    print(f'Ваша работа не удволитворительна, ваша выручка состовляет: {profit} руб.')
#elif profit > 0:
#    print(f'Хорошая работа, ваша выручка состовляет: {profit} руб.')
#elif profit == 0:
#    print(f'Вам надо поднапречься, ваша выручка составляет: {profit}  руб.')

#rab = int(input('Введите число работников работающих в вашей фирме: '))
#print(f'Прибыль {profit / rab} руб., составляет в расчёте на одного работника.')



a = int(input('В первый день пробежал бегун: '))
b = int(input('Километраж который должен достигнуть бегун: '))
day = 1
while a <= b:
    if a == b:
        break
    a += a / 10
    day += 1
print(f'На {day} день бегун достигнет своей цели.')
