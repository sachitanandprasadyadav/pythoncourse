import requests
from tabulate import tabulate
import json

# ----------------------------
# 1. OnlineKhabar Trending API
# ----------------------------
url1 = "https://www.onlinekhabar.com/wp-json/okapi/v1/trending-posts/?limit=3"

r = requests.get(url1)

if r.status_code == 200:
    print("\n=== Trending Posts ===")
    result = r.json()
    news = result.get('data', {}).get('news', [])

    for i in news:
        print("Post id:", i.get('post_id'))
        print("Link:", i.get('link'))
else:
    print("Failed to fetch trending posts")


# ----------------------------
# 2. NRB Forex API (Pagination + Tabulate)
# ----------------------------
header = ['ISO3', 'Name', 'Unit', 'Buy', 'Sell']

url = "https://www.nrb.org.np/api/forex/v1/rates?page=1&per_page=10&from=2025-03-01&to=2025-03-10"

while url:
    r = requests.get(url)

    if r.status_code != 200:
        print("Failed to fetch forex data")
        break

    data = r.json()

    payload = data['data']['payload']

    for item in payload:
        print("\nDate:", item['date'])

        table = []

        for rate in item['rates']:
            table.append([
                rate['currency']['iso3'],
                rate['currency']['name'],
                rate['currency']['unit'],
                rate['buy'],
                rate['sell']
            ])

        print(tabulate(table, headers=header, tablefmt="grid"))

    # move to next page
    url = data['pagination'].get('next')