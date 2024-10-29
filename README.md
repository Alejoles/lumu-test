# Backend Integrations Test

## Printed stats (if you run the code it will generate this)

```sh
Total records 16967

Client IPs Rank      Count      %
-------------------- ----- ------
111.90.159.121        3375  19.89%
45.231.61.2           1251   7.37%
187.45.191.2          1089   6.42%
190.217.123.244        738   4.35%
5.63.14.45             634   3.74%
-------------------- ----- ------

Host Rank                                          Count      %
-------------------------------------------------- ----- ------
pizzaseo.com                                        4626  27.26%
sl                                                  3408  20.09%
MNZ-efz.ms-acdc.office.com                            67   0.39%
global.asimov.events.data.trafficmanager.net          31   0.18%
www.google.com                                        30   0.18%
-------------------------------------------------- ----- ------
```

## Explain what is the computational complexity of your ranking algorithm.

Considering that we use pandas to perform most of the processing within a DataFrame, the read_and_process_file function, which is used at the beginning, would have a computational complexity of O(n) since creating the DataFrame with pd.read_csv would take O(n). Subsequently, we see pd.to_datetime(df[0] + ' ' + df[1]), which also has a complexity of O(n), as well as df[6].str.split("#", expand=True)[:][0], which again would have a complexity of O(n) due to the need to iterate through each entry and perform the split. Finally, df[9] and df[11] are constant operations since they only retrieve data from the already created DataFrame.



O(n) + O(n) + O(n) + O(1) + O(1) =



O(3n) + O(2) =



O(3n) = O(n), \text{ where } O(2) \text{ is constant, thus}



O(n) + O(2) = O(n) \text{ where } n \text{ is the size of queries.txt}


Similarly, the same would apply to print_client_ips_and_hosts_rank, since the only functions that have a complexity of O(n) would be data_ips.value_counts(), data_hosts.value_counts(), and the list comprehensions that iterate over ip_counts and name_counts. Since there is no complexity higher than O(n), we obtain a result of O(n) when summing them.

By combining both functions and their respective complexities, we find that both have O(n), so the final complexity is linear O(n).

```python

def print_client_ips_and_hosts_rank(data_ips, data_hosts):
    """
        This function is used to do the ranking of ips and hosts as
        requested by the test, it will print the data as tables.
    """
    ip_counts = data_ips.value_counts() # O(n)
    total_ips = len(data_ips) # O(1)
    data_client_ips = [(ip, count, round((count / total_ips) * 100, 2)) for ip, count in ip_counts.items()] # O(n)
    print(f"Total records {total_ips}\n") # O(1)
    print(f"{'Client IPs Rank':<20} {'Count':>5} {'%':>6}") # O(1)
    print(f"{'-'*20} {'-'*5} {'-'*6}") # O(1)
    for ip, count, percent in data_client_ips[:5]:  # O(5) o O(n) depending on how much data you want to see
        print(f"{ip:<20} {count:>5} {percent:>6}%") # O(1)
    print(f"{'-'*20} {'-'*5} {'-'*6}") # O(1)
    print() # O(1)
    name_counts = data_hosts.value_counts() # O(n)
    total_names = len(data_hosts) # O(1)
    data_host_rank = [(name, count, round((count / total_names) * 100, 2)) for name, count in name_counts.items()] # O(n)
    print(f"{'Host Rank':<50} {'Count':>5} {'%':>6}") # O(1)
    print(f"{'-'*50} {'-'*5} {'-'*6}") # O(1)
    for name, count, percent in data_host_rank[:5]: # O(5) o O(n) depending on how much data you want to see
        print(f"{name:<50} {count:>5} {percent:>6}%") # O(1)
    print(f"{'-'*50} {'-'*5} {'-'*6}") # O(1)

def read_and_process_file(file_name: str):
    df = pd.read_csv(file_name, sep=" ", header=None) # O(n)
    timestamps = pd.to_datetime(df[0] + ' ' + df[1]) # O(n)
    client_names = df[9] # O(1)
    client_ips = df[6].str.split("#", expand=True)[:][0] # O(n)
    query_type = df[11] # O(1)
    # O(n) + O(n) + O(n) + O(1) + O(1) =
    # O(3n) + O(2) =
    # O(3n) = O(n), O(2) still constant, then
    # O(n) + O(2) = O(n)  where n is the size of queries.txt
    # ---------- -------------- ------------
    print_client_ips_and_hosts_rank(client_ips, client_names)
    # ---------- -------------- ------------
```

## Provide instructions on how to run your script.

Create an .env file an fulfill the fields using the .env.example file as guide.

### Running with venv
(This commands are for ubuntu shell, may differ if you're using another OS)

First you have to create the virtual evironment.
```sh
python -m venv venv
```

Then you have to access to the virtual environment, type this command.

```sh
source venv/bin/activate
```

Once inside type the command that is next to "$" symbol.

```sh
(venv) $ pip install -r requirements.txt
```

```sh
(venv) $ python main.py
```

### Running with docker
(For all OS's)

Just run

```sh
docker-compose up --build
```

Docker will create an image and a container based in the information of Dockerfile and docker-compose.yml, it will run the command and then after finishes the execution the container will stop.