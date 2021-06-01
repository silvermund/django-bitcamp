import pandas as pd
from bs4 import BeautifulSoup
import requests


class Samsung(object):

    url = 'https://finance.naver.com/item/sise_day.nhn?code=005930'
    class_name = []
    driver = []
    title = []
    dict = []

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}').text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls = soup.find_all(name='tah p11', attrs=({"class":'span'}))
        for i in ls:
            self.title.append(i.find("num").text)

    def insert_dict(self):
        for i, j in enumerate(self.title):
            self.dict[j] = self.title[i]
        print(self.dict)

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/samsung.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

    @staticmethod
    def main():
        samsung = Samsung()
        while 1:
            menu = input('0-exit, 1-input time\n, '
                         '2-output\n, '
                         '3-print dict\n '
                         '4-dict to dataframe\n'
                         '5-df to csv')
            if menu == '0':
                break
            elif menu == '1':
                samsung.set_url('wl_ref=M_contents_03_01')
            elif menu == '2':
                samsung.class_name.append("title")
                samsung.get_ranking()
            elif menu == '3':
                samsung.insert_dict()
            elif menu == '4':
                samsung.dict_to_dataframe()
            elif menu == '5':
                samsung.df_to_csv()
            else:
                print('Wrong Number')
                continue

Samsung.main()