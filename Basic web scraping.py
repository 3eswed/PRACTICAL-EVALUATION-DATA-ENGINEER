import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    raise Exception("Failed to fetch the page. Check the URL and try again.")

soup = BeautifulSoup(response.content, 'html.parser')

people_also_watch_container = soup.find('div', {'data-reactid': '77'})

if people_also_watch_container is not None:
    companies_list = []

    for item in people_also_watch_container.find_all('a'):
        companies_list.append(item.text)
    
    df = pd.DataFrame(companies_list, columns=['Company'])
    # Save the CSV file to the specified directory
    save_path = "/Users/naseralausud/Desktop/Data Engineer/people_also_watch.csv"
    df.to_csv(save_path, index=False)
    print("Data has been scraped and saved to 'people_also_watch.csv'.")
else:
    print("Error: 'People Also Watch' section not found on the page. Please check the website's structure.")


