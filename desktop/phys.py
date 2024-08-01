#root.after(1000, click) #бесконечный цикл с прерыванием в секунду click - функция

Resist = 7 #сопротивление с ползунка меняем в пределах 0...20
eta = 0.5 #кпд в момент равенства сопротивлений

butt = False #логическая переменная, когда кнопка не была нажата

butt = not (butt) #при выполнении функции click при нажатии кнопки проводим инверсию логической переменной

def prog_load(butt, Resist): #функция движка лабораторной установки
    in_resist = 3.5  # внутреннее сопротивление источника
    edc = 6  # ЭДС в вольтах
    if butt:  # если кнопка активна
        eta = Resist / (Resist + in_resist)
        amperage = (edc - eta * edc) / in_resist
        voltage = amperage * Resist
    else:  # если кнопка не активна
        amperage = 0
        voltage = edc
    return round(amperage, 3), round(voltage,3)

U, I = prog_load(butt, Resist) #вывод напряжения и силы тока на приборы

print(U, I)
