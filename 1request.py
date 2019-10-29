def Opredelitel(c):
    '''Функция определяет високосный год или нет'''
    if c%4 !=0 or (c%100==0 and c%400 !=0):
        print('Не високосный')
    else:
        print('Високосный')
Opredelitel(2004)