import csv
from bs4 import BeautifulSoup
import requests
from urllib3.exceptions import InsecureRequestWarning



class Enter(object):

    HOST = "https://enter.kg/processory_bishkek"
    HEADERS = {

        'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'
        'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }

    def __init__(self,url,path) -> None:
        self.url = url
        self.path = path

    def parse(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.get(url = self.url,headers=self.HEADERS, verify=False)
        soup = BeautifulSoup(r.content,'html.parser')
        items = soup.find_all('div',class_ ='product vm-col vm-col-1')
        new_list = []
        for i in items:
            # try:
                new_list.append({
                    'title': i.find('span',class_ ='prouct_name').get_text(strip = True),
                    'image': self.HOST + i.find('a', class_ = 'product-image-link').find('img').get('src'),
                    'price': i.find('span',class_ ='price').get_text(strip=True),
                    'article':i.find('span',class_="sku").get_text(strip=True)
            })
            # except Exception as problem:
            #     print(f"{problem}")
        return new_list
    

    def save(self,items):
        with open(self.path,'w') as f:
            writer = csv.writer(f,delimiter=',')
            writer.writerow(['Название','Картинка','Цена'])
            for i in items:
                writer.writerow([i['title'],i['image'],i['price']])



enter = Enter(url = input("url....."),path ='{}.csv'.format(input("введите название файла")))
a = enter.parse()
enter.save(items=a)