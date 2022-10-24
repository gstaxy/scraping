import requests
import json
import pandas as pd

# URL to scrape: https://www.theglobeandmail.com/business/rob-magazine/top-growing-companies/article-canadas-top-growing-companies-meet-430-businesses-that-will-give-you/

url = "https://google-sheets-prod-dc5q4g5x5w7l.s3.ca-central-1.amazonaws.com/1ratXnMrRyCnnfYA2HL7cR5gm04ld_kvXMZKt6tWgneY.json"

payload = ""
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.7",
    "Connection": "keep-alive",
    "Origin": "https://www.theglobeandmail.com",
    "Referer": "https://www.theglobeandmail.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
}

# GET the response
response = requests.request("GET", url, data=payload, headers=headers)

# Keep the response in memory as a json
data = response.json()

# Save the json response locally
with open("data/tgam_top_growing_companies_2022.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# Get the header (column) list
columns = data["data"][0]["header"]
print(columns)

# Get all the companies in the "rows" list of the json file
all_companies = []
for company in data["data"][0]["rows"]:
    all_companies.append(company)

print(all_companies[:5])
print(len(all_companies))

# Save the json output to a csv file locally
df = pd.DataFrame(all_companies)
df.to_csv("data/tgam_top_growing_companies_2022.csv", header=columns, index=False)
