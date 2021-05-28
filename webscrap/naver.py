import pandas as pd
from bs4 import BeautifulSoup
import requests


class Naver(object):

    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = []
    driver = []
    title = []

    def set_url(self, detail):
        self.url = requests.get(f'{self.url}{detail}').text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls = soup.find_all(name='p', attrs=({"class": self.class_name[0]}))
        for i in ls:
            self.title.append(i.find("a").text)

    def insert_dict(self):
        for i, j in enumerate(self.title):
            self.dict[j] = self.title[i]
        print(self.dict)

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = './data/naver.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')

    @staticmethod
    def main():
        naver = Naver()
        while 1:
            menu = input('0-exit, 1-input time\n, '
                         '2-output\n, '
                         '3-print dict\n '
                         '4-dict to dataframe\n'
                         '5-df to csv')
            if menu == '0':
                break
            elif menu == '1':
                naver.set_url('wl_ref=M_contents_03_01')
            elif menu == '2':
                naver.class_name.append("title")
                naver.get_ranking()
            elif menu == '3':
                naver.insert_dict()
            elif menu == '4':
                naver.dict_to_dataframe()
            elif menu == '5':
                naver.df_to_csv()
            else:
                print('Wrong Number')
                continue

Naver.main()