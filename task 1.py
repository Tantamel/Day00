number = input ('Введите сколько дней в феврале: ')
if number == '28':
    def total_time_of_working(days):
        a = 12 * (days // 4 * 2 + min(days % 4, 2))
        return a

    print(f'Первый сотрудник отработал за месяц: {total_time_of_working(28)} часов')
    print(f'Второй сотрудник отработал за месяц: {total_time_of_working(27)} часов')
    print(f'Третий сотрудник отработал за месяц: {total_time_of_working(26)} часов')
    print(f'Четвертый сотрудник отработал за месяц: {total_time_of_working(25)} часов')

    print(f'Общее количество отработанных часов: {total_time_of_working(28) + total_time_of_working(27) + total_time_of_working(26) + total_time_of_working(25)}')

elif number == '29':
    def total_time_of_working (days):
        a = 12*(days//4*2 + min(days % 4, 2))
        return a

    print (f'Первый сотрудник отработал за месяц: {total_time_of_working (29)} часов')
    print (f'Второй сотрудник отработал за месяц: {total_time_of_working (28)} часов')
    print (f'Третий сотрудник отработал за месяц: {total_time_of_working (27)} часов')
    print (f'Четвертый сотрудник отработал за месяц: {total_time_of_working (26)} часов')

    print (f'Общее количество отработанных часов: {total_time_of_working (29) + total_time_of_working (28) + total_time_of_working (27) + total_time_of_working (26)}')
else:
    print ('Неверный ввод. В феврале 28 или 29 дней')