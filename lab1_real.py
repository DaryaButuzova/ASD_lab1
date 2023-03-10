#Натуральные числа. Выводит на экран число и его прямой, обратный и дополнительный коды (бинарные).
dict= {
    0:'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
    6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
    11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать',
    16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать',
    24: 'двадцать четыре', 1010: 'Тысяча десять',
}

buffer_len = 1
work_buffer = ""

with open("text.txt","r") as file: #открываем файл
    print("Результат работы программы")
    buffer = file.read(buffer_len)
    #print(buffer)
    if not buffer: #если файл пустой
        print("файл пустой")
    while buffer: #пока файл не пустой
        while buffer >='0' and buffer <= '9':
            if buffer >= '0' and buffer <= '9':
                work_buffer += buffer
                #print('рабочий буфер -', work_buffer)
            buffer = file.read(buffer_len) #читаем очередной блок
        if len(work_buffer) > 0:
            #print(work_buffer)

            print(work_buffer)
            r = bin(int(work_buffer))[2:]
            print("Прямой, обратный и дополнительный код для", work_buffer, " --->", r)
        work_buffer = ''

        buffer = file.read(buffer_len) # читаем очередной блок
    else:
        print('Файл пустой или нет чисел удовлет. условию')
