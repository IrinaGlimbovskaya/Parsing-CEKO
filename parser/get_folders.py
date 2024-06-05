#== программа для формирования списка каталогов с рисунками
#== А.Б.Глазов 02/03/2021

#-- подключить библиотеки
import os
        
#== прочитать список подкаталогов с заданиями
data_path = "C:\Users\Irina\Desktop\kursovaya\parsing"
os.chdir(data_path)

data_path = os.getcwd()
print(data_path)

entries = os.listdir('.')
dir_list = [entry for entry in entries if os.path.isdir(entry)]
print(dir_list)

#== записать в файл список подкаталогов
fh = open("dir_list.txt","w")
for entry in dir_list:
    fh.write(entry+"\n")
fh.close()

