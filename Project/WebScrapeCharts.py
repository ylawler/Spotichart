from bs4 import BeautifulSoup
import requests


class WebScrapeCharts():

    def __init__(self):
        self.url = 'https://spotifycharts.com/regional/'
        self.song_ids = dict()
        self.song_ids_array = []

    def __generate_url(self, country_code, recurrence):
        self.url += (country_code + '/' + recurrence + '/' + 'latest')

    def get_charts(self, country_code, recurrence):
        # generate the url
        self.__generate_url(country_code, recurrence)

        response = requests.get(self.url)

        html_soup = BeautifulSoup(response.text, 'html.parser')
        song_containers = html_soup.find_all('td', class_='chart-table-image')

        for song_container in song_containers:
            href = song_container.a['href']
            song_id = href.split('/')[-1]
            self.song_ids[song_id] = href
            self.song_ids_array.append(song_id)

        return len(self.song_ids_array) == 200

    def save_for_testing(self, country_code, recurrence):
        if self.get_charts(country_code, recurrence):
            # create filename to save based on country code, recurrence and date
            filename = 'test_' + country_code + '_' + recurrence + '.txt'
            with open(filename, 'a') as af:
                for song_id in self.song_ids_array:
                    if song_id == self.song_ids_array[-1]:
                        af.write(song_id)
                    else:
                        af.write(song_id + '\n')
            return True
        else:
            return False

    def load_ids_from_file(self, country_code, recurrence):
        if self.is_empty():
            try:
                filename = 'test_' + country_code + '_' + recurrence + '.txt'
                with open(filename, 'r') as rf:
                    for line in rf:
                        self.song_ids_array.append(line.strip('\n'))
                return True
            except:
                return False
        else:
            return False

    def is_empty(self):
        return len(self.song_ids_array) == 0

    def set_default(self):
        self.url = 'https://spotifycharts.com/regional/'
        self.song_ids_array = []