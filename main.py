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
        This function is used to do the ranking of ips and hosts as
        requested by the test, it will print the data as tables.
    """
    # Counting the occurrences of each IP
    ip_counts = data_ips.value_counts()
    total_ips = len(data_ips)

    # Calculate the percentage of each IP
    data_client_ips = [(ip, count, round((count / total_ips) * 100, 2)) for ip, count in ip_counts.items()]
    print(f"Total records {total_ips}\n")
    # Print first 5 results in table format
    print(f"{'Client IPs Rank':<20} {'Count':>5} {'%':>6}")
    print(f"{'-'*20} {'-'*5} {'-'*6}")
    for ip, count, percent in data_client_ips[:5]:
        print(f"{ip:<20} {count:>5} {percent:>6}%")
    print(f"{'-'*20} {'-'*5} {'-'*6}")

    print()

    # Count the occurrences of each client_name
    name_counts = data_hosts.value_counts()
    total_names = len(data_hosts)

    # Calculate the percentage of each client_name
    data_host_rank = [(name, count, round((count / total_names) * 100, 2)) for name, count in name_counts.items()]


    # Print first 5 results in table format
    print(f"{'Host Rank':<50} {'Count':>5} {'%':>6}")
    print(f"{'-'*50} {'-'*5} {'-'*6}")
    for name, count, percent in data_host_rank[:5]:
        print(f"{name:<50} {count:>5} {percent:>6}%")
    print(f"{'-'*50} {'-'*5} {'-'*6}")


def read_and_process_file(file_name: str):
    """
        Main processing function, this function uses pandas to retrieve the
        data from queries.txt file, then it
        Args:
            file_name (str): (the name of the file, in this case queries.txt)
        returns:
            records (list): a list of objects(dicts) that contains the data to do the requests
                to the API.
    """
    df = pd.read_csv(file_name, sep=" ", header=None)
    # the API needs the next data:
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
    """
    Sends batches of DNS queries to a specified API endpoint.

    Args:
        data (list): A list of DNS query data to be sent in batches.

    """
    headers = {'Content-Type': "application/json"}
    url_parsed = f"{API_URL}/collectors/{COLLECTOR_ID}/dns/queries?key={LUMU_CLIENT_KEY}"
    sending_size = 500
    ammount_of_blocks = math.ceil(len(data) / sending_size)
    for i in range(ammount_of_blocks):
        # Slice the data list to get the current batch
        data_to_json = data[i*sending_size:(i+1)*sending_size]
        # Send a POST request to the API with the current batch of data
        response = requests.post(url=url_parsed, headers=headers, json=(data_to_json))
        # Optionally print the length of the current batch for debugging purposes
        # print(len(data_to_json))  # To ensure the last batch is less than or equal to 50


if __name__ == "__main__":
    data_list = read_and_process_file("queries.txt")
    make_requests(data_list)
