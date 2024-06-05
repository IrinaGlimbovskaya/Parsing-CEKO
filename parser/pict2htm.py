#== программа для преобразования рисунков страниц в текстовый вид
#== А.Б.Глазов 02/03/2021

#-- подключить библиотеки
import os
import time
        
#== прочитать список подкаталогов с заданиями
#data_path = "f:\work\2021\PROJ\pr01b\"
'''
data_path = "f:/work/2021/PROJ/pr01b/"
os.chdir(data_path)
'''
data_path = os.getcwd()
print(data_path)

fh = open("dir_list.txt")
dir_list = fh.readlines()
fh.close()
for num in range(len(dir_list)):
    dir_list[num] = dir_list[num].strip()
print(dir_list)

#== засечка времени начала
time_beg = int(time.time())
print("time_beg = ", time_beg)

#== цикл по всем подкаталогам для текстов
print("convert to *.htm")
cmd_path = '"c:/Program Files/ABBYY FineReader 12/FineCmd.exe"'
for sub_dir in dir_list:
        filtxt_name = data_path + "/"+sub_dir[-2:]+ ".htm"
        os.chdir(sub_dir)
        print( os.getcwd())
        entries = os.listdir('.')
        pict_files = [entry for entry in entries if entry[-3:] == "jpg"]

        path_all = cmd_path + " " +" ".join(pict_files)+ " /lang Mixed /out " + \
                   filtxt_name + " /quit"
        os.system(path_all)
        
        os.chdir("..")


#== засечка времени окончания
time_end = int(time.time())
print("time_end = ", time_end)
        
print("delta_t(sec) = ", time_end - time_beg )        

