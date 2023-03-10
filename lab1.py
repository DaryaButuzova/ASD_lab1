max_buffer_len = 100
buffer_len = 1

work_buffer = ""
engl_flag = False
work_buffer_len = buffer_len

try:
    with open("text.txt") as file:
        print("Результат работы программы")
        buffer = file.read(buffer_len)
        #print(buffer)
        if not buffer:
            print("файл пустой")
        while buffer:
            #print('буффер',buffer)
            if buffer>='0' and buffer <='9':
                engl_flag= True
                work_buffer += buffer.upper()

            else:
                work_buffer += buffer
                #print('рабочий буфер -',work_buffer )
                if work_buffer >= 'A' and buffer <= 'Z':
                    engl_flag = True
                    #print(buffer,work_buffer,engl_flag,work_buffer_len)

            if buffer.find(" ") >= 0:
                if engl_flag == False:
                    #print(work_buffer)
                    engl_flag = False
                work_buffer = " "
                work_buffer_len = 0
            buffer = file.read(buffer_len)
            work_buffer_len += buffer_len
            if work_buffer_len>= max_buffer_len and buffer.find(".")<0 and buffer.find("!")<0 and buffer.find("?")<0:
                print("\nфайл .txt не содержит знаков окончания ")
                buffer = ""
except FileNotFoundError:
    print("файл в директории проекта не обнаружен ")