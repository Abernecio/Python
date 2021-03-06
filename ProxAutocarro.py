from bs4 import BeautifulSoup
import requests
import pandas as pd

data = requests.get('http://www.stcp.pt/pt/itinerarium/soapclient.php?codigo=AAL1').content #Faz um GET a pagina
soup = BeautifulSoup(data, 'html.parser') #Faz sopinha

table = soup.find_all('table', {'id': 'smsBusResults'}) #Vai buscar a tabela com o id smsBusResults

tr = table[0].find_all('tr') # Asssocia todos os tr (rows) da tabela a variavel tr


headers = [] # Lista de cabecalhos
for td in tr[0].find_all('th'):
    headers.append(td.text)
temp_df = pd.DataFrame(columns=headers) # Procura o cabecalho e define-o como colunas


pos = 0
for i in range(1, len(tr)):
    temp_list = []
    for td in tr[i].find_all('td'):
        value = td.text.replace('\n', '')
        value = value.replace('\t', '')
        value = value.replace('-', '')
        temp_list.append(value)
    temp_df.loc[pos] = temp_list
    pos += 1

print(temp_df)
