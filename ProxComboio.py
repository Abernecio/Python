import requests
import os
import string
from bs4 import BeautifulSoup
import datetime
import time
import lxml


def get_todays_trains():
    now = datetime.datetime.now()

    url = 'https://www.cp.pt/sites/passageiros/en/train-times/Train-time-results'

    r = requests.post(url, allow_redirects=False, data={
        'arrival': 'Porto - Campanha',
        'depart': 'Aguas Santas - Palmilheira',
        'departDate': str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    })

    html = r.text
    soup = BeautifulSoup(html, features='lxml')

    for row in soup.findAll('table')[1].tbody.findAll('tr'):
        depart = row.findAll('td')[2].text.split()
    print(depart)
    return depart
