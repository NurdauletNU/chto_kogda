# Todo работа с текстовыми файлами

# режимы файлов w-запись, r-чтение, a-добавить, wb-запись в байтах, rb-чтение в байтах

# ручное закрытие файла
#file1=open("z_new.txt", mode="w")
#file1.write("Python is awesome!123\n\thi")
#file1.close()


#file1=open("z_new.txt",mode="a")
#file1.write(" Hello")
#file1.close()


# try:

    # file1=open("net.txt", mode="w")
    # file1.write("Pyton is awesime")
# except Exception as error:
    # print(error)
# else:
     # pass
# finally:
    # file1.close



# Контекстный менеджер - файл закрывается сам всегда

with open("z_new.txt", mode="r") as file2:
    line1=file2.read()
    print(line1)
    line2=file2.readlines()
    print(line2)
