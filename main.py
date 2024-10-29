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
    data = [(ip, count, round((count / total_ips) * 100, 2)) for ip, count in ip_counts.items()]

    # Imprimir resultados en formato de tabla
    print(f"{'Client IP':<20} {'Count':>5} {'%':>6}")
    print(f"{'-'*20} {'-'*5} {'-'*6}")
    for ip, count, percent in data[:5]:
        print(f"{ip:<20} {count:>5} {percent:>6}%")
    print(f"{'-'*20} {'-'*5} {'-'*6}")



def make_requests():
    pass


if __name__ == "__main__":
    read_and_process_file("queries.txt")