import requests
from bs4 import BeautifulSoup
import datetime
import calendar

url_stations = 'https://www.cp.pt/sites/spring/stations'

r_stations = requests.get(url_stations)

stations = r_stations.json()


def get_todays_trains(depart, arrival):

    get_todays_trains.depart = stations
    get_todays_trains.arrival = stations
    now = datetime.datetime.now()
    dayn = now.day
    monthno = now.month
    yearno = now.year

    url = 'https://www.cp.pt/sites/passageiros/en/train-times/Train-time-results'

    r = requests.post(url, allow_redirects=False, data={
        'arrival': arrival,
        'depart': depart,
        'date': str(dayn) + ' ' + calendar.month_name[monthno] + ', ' + str(yearno),
        'departDate': str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    })

    html = r.text
    soup = BeautifulSoup(html, features='lxml')

    train_data = dict()
    train_data['departing_date'] = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    train_data['departing_trains'] = []
    for row in soup.findAll('table')[1].tbody.findAll('tr'):
        depart = row.findAll('td')[2].text.split()
        train_data['departing_trains'].append(depart)
    print(train_data)
    return train_data


get_todays_trains('Porto - Campanha', 'Porto - Sao Bento')
