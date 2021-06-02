import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

class Samsung2(object):

    i = 0


    url = 'https://finance.naver.com/item/frgn.nhn?code=005930'
    class_name = ''
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    dic = {}
    ls = []
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        ls1 = soup.find_all('tc', {'class': 'tc'})
        ls2 = soup.find_all('tc', {'class': 'num'})
        for i in ls1:
            self.day.append(i.find('span').text)
        for i in ls2:
            self.price.append(i.find('span').text)

    def scrap_to_dict(self):
        dic = dict(zip(self.day, self.price))
        print(dic)

    def dict_to_dataframe(self):
        dt = self.dic
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/samsung2.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

Samsung2().scrap()
Samsung2().scrap_to_dict()
Samsung2().dict_to_dataframe()
Samsung2().df_to_csv()