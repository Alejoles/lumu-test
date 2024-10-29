import pandas as pd
from settings import (
    LUMU_CLIENT_KEY,
    COLLECTOR_ID,
    API_URL,
)

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

    # Contar las ocurrencias de cada IP
    ip_counts = client_ips.value_counts()
    total_ips = len(client_ips)

    # Calcular el porcentaje de cada IP
    data_client_ips = [(ip, count, round((count / total_ips) * 100, 2)) for ip, count in ip_counts.items()]

    # Imprimir primeros 5 resultados en formato de tabla
    print(f"{'Client IP':<20} {'Count':>5} {'%':>6}")
    print(f"{'-'*20} {'-'*5} {'-'*6}")
    for ip, count, percent in data_client_ips[:5]:
        print(f"{ip:<20} {count:>5} {percent:>6}%")
    print(f"{'-'*20} {'-'*5} {'-'*6}")

    print()

     # Contar las ocurrencias de cada client_name
    name_counts = client_names.value_counts()
    total_names = len(client_names)

    # Calcular el porcentaje de cada client_name y tomar solo los primeros 5
    data_host_rank = [(name, count, round((count / total_names) * 100, 2)) for name, count in name_counts.items()]


    # Imprimir primeros 5 resultados en formato de tabla
    print(f"{'Host Rank':<50} {'Count':>5} {'%':>6}")
    print(f"{'-'*50} {'-'*5} {'-'*6}")
    for name, count, percent in data_host_rank[:5]:
        print(f"{name:<50} {count:>5} {percent:>6}%")
    print(f"{'-'*50} {'-'*5} {'-'*6}")






def make_requests():
    pass


if __name__ == "__main__":
    read_and_process_file("queries.txt")