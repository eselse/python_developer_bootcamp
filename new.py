from time import time
import requests
import time
from prettytable import PrettyTable

repos_set = set()
# table = PrettyTable()
# table.field_names = ["Repository Name"]

# query = "python"
# first page
# page = 1

# # search for the top repositories
# api_url = f"https://api.github.com/search/repositories?q={query}&{page}"

# # send get request
# response = requests.get(api_url)

# # get the json data
# data = response.json()

# for repository in data["items"]:
#     name = repository["full_name"]
#     # table.add_row([name])
#     # repos_set.add(name)

# # print(table)
# print(repos_set)
f = open("links.txt", "a")
for page in range(1, 101):
    table = PrettyTable()
    table.field_names = ["Repository Name"]

    query = "python"
    api_url = f"https://api.github.com/search/repositories?q={query}&{page}"
    # send get request
    response = requests.get(api_url)

    # get the json data
    data = response.json()

    try:
        for repository in data["items"]:
            name = repository["full_name"]
            # table.add_row([name])
            repos_set.add(name)

    except Exception as ex:
        # print(ex)
        # print(table)
        # print(page)
        time.sleep(1)

    time.sleep(1)
print(repos_set)
for repo in repos_set:
    f.write(f"{repo}\n")
