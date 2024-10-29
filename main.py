import pandas as pd
from .settings import (
    LUMU_CLIENT_KEY,
    COLLECTOR_ID,
    API_URL,
)

def read_and_process_file(file_name):
    df = pd.read_csv(file_name, sep=" ", header=None)
    # La API necesita los siguientes datos:
    #   timestamp(datetime), name(Array), client_ip(str), client_name(str), type(str)
    timestamps = pd.to_datetime(df[0] + ' ' + df[1])
    # print(timestamps)
    client_names = df[9]
    client_ips = df[6].str.split("#")[:][0]


def make_requests():
    pass


if __name__ == "__main__":
    read_and_process_file("queries.txt")