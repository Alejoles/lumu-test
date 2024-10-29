# Backend Integrations Test


## Explain what is the computational complexity of your ranking algorithm.


```python
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