"""
take a website name, split it and make an async request, searching
for all the emails in the domain.
"""
import csv
import os
import time
from tldextract import extract
from collections import OrderedDict
import requests

# constants
file_path = '/media/alxfed/toca/aa-crm/other-lists/08122019_archs_interor.csv'
api_url = 'https://api.anymailfinder.com/v4.1/search/company.json'
api_key = os.environ['API_KEY']
headers = {'X-Api-Key': api_key}

# check the credits
rows = OrderedDict()
fieldnames = []

with open(file_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        if not row['Website']:  # check whether there is a website
            row.update({'emails': ''})
            pass
        else:
            tsd, td, tsu = extract(row['Website'])  # tldextract
            payload = {'domain': td + '.' + tsu,
                       'company_name': row['Name']}
            r = requests.post(api_url, headers=headers,
                              json=payload, timeout=60)
            if r.status_code > 202:
                """errors
                """
                print('errors happened!')
                pass
            elif r.status_code < 203:
                while r.status_code != 200:
                    time.sleep(3)
                    r = requests.request('POST', api_url,
                                         headers=headers, json=payload)
                    if r.status_code == 200:
                        break
                resp = r.text.json()
                row['emails'] = resp
            else:
                print('I dunno what this is...', r.status_code)
                pass
        rows.update(row)
    fieldnames = f_csv._fieldnames


with open(file_path,'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
print('ok')