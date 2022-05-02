
import pandas as pd
import sqlite3
from pyModbusTCP.client import ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient
import time


while True:
    c = ModbusClient()
    c.host("10.180.1.250")
    c.port(502)
    c.unit_id(255)
    ip_address = "10.180.1.250"
    client = ModbusTcpClient(ip_address)

    if not c.open():
        print('Não foi possível obter o status da linha')
    if c.is_open():
        status_linha = c.read_coils(40008, 1)
        if status_linha:
            if status_linha[0] == True:
                while status_linha[0] == True:
                    print('Testando...')
                    time.sleep(1)
                    status_linha = c.read_coils(40008, 1)
                    if status_linha[0] == False:
                        break
                print('TESTADO')
                status_linha = ['Testado...']
                tabela = pd.DataFrame({'Teste': status_linha})
                connection = sqlite3.connect('testes.db')
                con = connection.cursor()
                def create_table():
                    con.execute('CREATE TABLE IF NOT EXISTS dados (Teste text)')
                create_table()
                tabela.to_sql(name = 'dados', con = connection, if_exists = 'append', index = False)
                
            elif status_linha[0] == False:
                print('Ociosa...')
                status_linha = 'Ociosa'
        else:
            print('Não foi possível obter o status da linha')
    time.sleep(1.5)

    # simulando dados recebidos e criando um data frame

    

 
