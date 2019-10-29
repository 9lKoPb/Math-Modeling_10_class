from PhyConst import g
def FullEnergy(m, h, v):
    '''Функция определяет полную механическую энергию тела, брршенного над Землей
    m-масса h-высота v-cкорость
    '''
    x = m*g*h + (m*v**2)/2
    print(x, 'Дж')
FullEnergy(50, 200, 3)  