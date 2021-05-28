import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

class NaverMovie(object):

    i = 0


    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = ''
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    dict = {}
    ls = []
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {"class":self.class_name})
        for i in all_div:
            self.ls.append(i.find("a").text)
        driver.close()

    def insert_dict(self):
        for i, j in enumerate(self.ls):
            self.dict[i] = j
        print(dict)

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/naver_movie.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

if __name__ == '__main__':
    naver = NaverMovie()
    naver.class_name = input('input_class') # 'tit3'
    naver.scrap()
    naver.insert_dict()
    naver.dict_to_dataframe()
    naver.df_to_csv()
