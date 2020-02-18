# -*- coding: utf-8 -*-
import os
import csv
import json
from uuid import uuid4
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor,as_completed

def get_time_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def download_file(row):
    file_name = f"{row['year']}-contratos-convenios-e-parcerias"

    ROOT_DIR = os.path.realpath(os.path.dirname(__file__))
    CSV_FILE = f'{file_name}.csv'

    if not os.path.isfile(f'{ROOT_DIR}/{CSV_FILE}'):

        print(f"{get_time_now()} downloading file {row['url']}")
        with requests.get(row['url']) as r:
            with open(f'{ROOT_DIR}/{CSV_FILE}', 'wb') as f:
                f.write(r.content)
                f.close()
                print(f"{get_time_now()} download Ok {CSV_FILE}")

    with open(f'{ROOT_DIR}/{CSV_FILE}', 
            encoding='utf-8', errors='ignore') as f:

        reader = csv.reader(f, delimiter=';')
        first = True
        second = True

        for row in reader:
            if not first:
                if not second:
                    orgao = row[0]
                    retranca = row[1]
                    modalidade = row[2]
                    numero_licitacao = row[3]
                    numero_processo = row[4]
                    evento = row[5]
                    objeto = row[6]
                    data_publicacao_extrato = row[7]
                    fornecedor = row[8].strip()
                    fornecedor_tipo = row[9].strip()
                    fornecedor_documento = row[10].strip()
                    data_assinatura_extrato = row[11].strip()
                    validade_extrato = row[12]
                    tipo_validade_extrato = row[13]
                    valor_contrato = row[14]
                    numero_contrato = row[16]

                    dict_payroll = { 
                        'orgao': orgao, 
                        'retranca': retranca, 
                        'modalidade': modalidade, 
                        'numero_licitacao': numero_licitacao, 
                        'numero_processo': numero_processo, 
                        'evento': evento, 
                        'objeto': objeto, 
                        'data_publicacao_extrato': data_publicacao_extrato, 
                        'fornecedor': fornecedor, 
                        'fornecedor_tipo': fornecedor_tipo, 
                        'fornecedor_documento': fornecedor_documento, 
                        'data_assinatura_extrato': data_assinatura_extrato, 
                        'validade_extrato': validade_extrato, 
                        'tipo_validade_extrato': tipo_validade_extrato, 
                        'valor_contrato': valor_contrato, 
                        'numero_contrato': numero_contrato 
                    }
                    
                    # hashing json file name with uuid
                    hash = uuid4().hex.lower()
                    
                    file_json = f'{ROOT_DIR}/data/{hash}.json'

                    # save file 
                    with open(file_json, mode="w") as f:
                        f.write(json.dumps(dict_payroll, indent=4))

                    print(f'{get_time_now()} [ Ok ] {hash} {numero_processo}')

                else:
                    second = not second
            else:
                first = not first

    return f'{CSV_FILE}'

#===============================================================================
if __name__ == '__main__':
    print(f"{get_time_now()} Starting... ")

    URL = 'http://dados.prefeitura.sp.gov.br'
    URL = f'{URL}/dataset/base-de-compras-e-licitacoes'

    yearOfPayroll = [ '2017' ] # just one
    links = []

    print(f"{get_time_now()} yearOfPayroll {yearOfPayroll}")

    # getting page content
    result = requests.get(URL)

    # parsing
    soup = BeautifulSoup(result.text, features='html.parser')

    for el in soup.select('ul.resource-list li.resource-item'):
        year = el.find('a', { 'class': 'heading'})['title'][-4:]
        url = el.find('a', { 'class': 'resource-url-analytics'})['href']

        if year in yearOfPayroll and '.csv' in url:
            links.append({ 'year': year, 'url': url})

    # threading in python to run faster (asynchronous)
    with ThreadPoolExecutor(max_workers=3) as executor:
        for thread in as_completed({ 
                executor.submit(download_file, row): row for row in links 
            }):
            try:
                thread.result()
            except Exception as e:
                print(f"{get_time_now()} ERROR {e}")

    exit(0)