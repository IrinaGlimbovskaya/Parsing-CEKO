import requests as rq
from bs4 import BeautifulSoup as bs
import os

#== функции

#-- считать картинку в файл с указанием каталога
def save_pict( img_src, dir_name):
        img_url = url_root + img_src.strip()
        #print(img_url)
        file_name = img_url.split('_')[-1].strip()
        path = dir_name + "/"+ file_name
        print(path)

        img = rq.get(img_url)
        out = open(path, "wb")
        out.write(img.content)
        out.close()
        
#-- считать в файлы все картинки страницы указанием каталога
def read_allpictures(link):
        dir_name = link.text.strip()
        loc_url =  url_root + link['href'].strip()
        loc_resp = rq.get(loc_url)
        loc_soup = bs(loc_resp.text,"html.parser")
        images = loc_soup.select("img")
        for image in images:
                if 'uploads' in image['src']:
                        save_pict( image['src'], dir_name)
                
        
#== прочитать страницу си списком всех заданий  
url_root = "http://ceko-pmr.org"
url_alltest = "http://ceko-pmr.org/Home/PodgotKEGE?current=%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%5C%D0%91%D0%B0%D0%BD%D0%BA%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B9%20%D0%95%D0%93%D0%AD%5C%D0%9E%D0%9E%D0%9E%20%D1%81%20%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%BC%20%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%BC%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F"
resp = rq.get(url_alltest)
print(resp.status_code)
text = resp.text
print(len(text))

#== сохранить ее для контроля на диск
fh = open("alltest.txt","w",encoding ="utf8")
fh.write(text)
fh.close()

#== выбрать все ссылки на задания
soup = bs(resp.text,"html.parser")
links = soup.select("a.section-link")
print( "testlinks_count: ", len(links))

#== создать каталоги для всех страниц заданий
for link in links:
        dir_name = link.text.strip()
        print (dir_name)
        try:
                os.mkdir(dir_name)
        except:
                pass

#== пройти по всем страницам и считать все рисунки с заданиями
for link in links:
        read_allpictures(link)

        
