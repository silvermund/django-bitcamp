from bs4 import BeautifulSoup
import requests


class Melon(object):
    url = 'https://www.melon.com/chart/index.htm?dayTime='
    header = {'User-Agent': 'Mozilla/5.0'}
    class_name = []

    def set_url(self,time):
        self.url = requests.get(f'{self.url}{time}', hea)