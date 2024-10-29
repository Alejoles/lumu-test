import pandas as pd
import json
import requests
import math
from settings import (
    LUMU_CLIENT_KEY,
    COLLECTOR_ID,
    API_URL,
)

def print_client_ips_and_hosts_rank(data_ips, data_hosts):
    """
        Esta función sirve únicamente para mostrar los datos
        ordenados de la forma en la que se pide en el ejercicio
    """
    # Contar las ocurrencias de cada IP
    ip_counts = data_ips.value_counts()
    total_ips = len(data_ips)

    # Calcular el porcentaje de cada IP
    data_client_ips = [(ip, count, round((count / total_ips) * 100, 2)) for ip, count in ip_counts.items()]

    # Imprimir primeros 5 resultados en formato de tabla
    print(f"{'Client IPs Rank':<20} {'Count':>5} {'%':>6}")
    print(f"{'-'*20} {'-'*5} {'-'*6}")
    for ip, count, percent in data_client_ips[:5]:
        print(f"{ip:<20} {count:>5} {percent:>6}%")
    print(f"{'-'*20} {'-'*5} {'-'*6}")

    print()

     # Contar las ocurrencias de cada client_name
    name_counts = data_hosts.value_counts()
    total_names = len(data_hosts)

    # Calcular el porcentaje de cada client_name y tomar solo los primeros 5
    data_host_rank = [(name, count, round((count / total_names) * 100, 2)) for name, count in name_counts.items()]


    # Imprimir primeros 5 resultados en formato de tabla
    print(f"{'Host Rank':<50} {'Count':>5} {'%':>6}")
    print(f"{'-'*50} {'-'*5} {'-'*6}")
    for name, count, percent in data_host_rank[:5]:
        print(f"{name:<50} {count:>5} {percent:>6}%")
    print(f"{'-'*50} {'-'*5} {'-'*6}")


def read_and_process_file(file_name):
    df = pd.read_csv(file_name, sep=" ", header=None)
    # La API necesita los siguientes datos:
    #   timestamp(datetime), name(Array), client_ip(str), client_name(str), type(str)
    timestamps = pd.to_datetime(df[0] + ' ' + df[1])
    # print((timestamps))
    client_names = df[9]
    # print(client_names)
    client_ips = df[6].str.split("#", expand=True)[:][0]
    # print(client_ips)
    query_type = df[11]
    # print(query_type)
    # ---------- -------------- ------------
    print_client_ips_and_hosts_rank(client_ips, client_names)
    # ---------- -------------- ------------
    print(len(df))
    records = []
    for index in range(len(df)):
        record = {
            "timestamp": timestamps[index].strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "name": client_names[index],
            "client_name": client_names[index],
            "client_ip": client_ips[index],
            "type": query_type[index]
        }
        records.append(record)

    return records



def make_requests(data: list):
    headers = {'Content-Type': "application/json"}
    url_parsed = f"{API_URL}/collectors/{COLLECTOR_ID}/dns/queries?key={LUMU_CLIENT_KEY}"
    sending_size = 300
    ammount_of_blocks = math.ceil(len(data) / sending_size)
    for i in range(ammount_of_blocks):
        data_to_json = data[i*sending_size:(i+1)*sending_size]
        # print(len(data_to_json)) # Para ver que el último dato sea menor o igual a 500
        response = requests.post(url=url_parsed, headers=headers, json=(data_to_json))
        print(response.status_code)
        print(response.text)


if __name__ == "__main__":
    data_list = read_and_process_file("queries.txt")
    make_requests(data_list)
