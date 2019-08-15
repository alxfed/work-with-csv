import csv
import os
import time
from tldextract import extract
import requests


api_key = os.environ['API_KEY']
api_url = 'https://api.anymailfinder.com/v4.1/search/company.json'
headers = {'X-Api-Key': api_key}
website = 'https://www.t2kproperties.com'
company = ''

tsd, td, tsu = extract(website)  # tldextract

payload = {'domain': td + '.' + tsu,
           'company_name': company}
r = requests.post(api_url, headers=headers, data=payload, timeout=60)

resp = r.json()