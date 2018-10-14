import requests
from bs4 import BeautifulSoup


def get_next_bus(stopcode):
    stopcode = 'JDEU4'
    url = 'http://www.stcp.pt/pt/itinerarium/soapclient.php?codigo=' + stopcode
    err60 = 'Nao ha autocarros nos proximos 60 minutos'
    err404 = 'Paragem nao encontrada'

    r = requests.get(url, data={
        'codigo': stopcode
    })

    html = r.text
    soup = BeautifulSoup(html, features='lxml')

    if soup.find('Por favor, utilize o codigo SMSBUS indicado na placa da paragem..'):
        print(err404)
        # return err404
    elif soup.find('Nao ha autocarros previstos para a paragem indicada nos proximos 60 minutos.'):
        print(err60)
        # return err60

    for row in soup.findAll('table'):
        depart = row.findAll('td')[1].text.split()
        print(depart)
        return depart

get_next_bus('JDEU4')

if sonme]
dkdf

