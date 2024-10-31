import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"
URL = "https://customsearch.googleapis.com/customsearch/v1"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"
QUERY = "student internship"

PARAMETERS = {
    "key": API_KEY,
    "cx": SEARCH_ENGINE_ID,
    "q": QUERY,
    "num": 10
}

response = requests.get(URL, params=PARAMETERS)
data = response.json()

structured_data = []
for item in data.get('items', []):
    item_data = {
        'TITLE': item.get('title', 'N/A'),
        'LINK': item.get('link', 'N/A'),
        'DISPLAYLINK': item.get('displayLink', 'N/A')
    }
    structured_data.append(item_data)

df = pd.DataFrame(structured_data)
df.to_csv("Inters_Websites_1.csv", index=False)
