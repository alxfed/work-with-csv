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
output_file_path = '/media/alxfed/toca/aa-crm/other-lists/archs_with_emails.csv'
credits_check_url = 'https://api.anymailfinder.com/v4.1/account/hits_left.json'
api_url = 'https://api.anymailfinder.com/v4.1/search/company.json'
api_key = os.environ['API_KEY']
# use this header with all the API calls
headers = {'X-Api-Key': api_key}

# check the number of credits left
r = requests.get(credits_check_url, headers=headers)
if r.status_code==200:
    resp = r.json()
    number = resp['credits_left']
    if number <=100:
        print("Less than 100 credits! I'm not working!")
        exit()
    else:
        print(number, 'credits left')
else:
    print('The API key is not working.')
    exit()

rows = OrderedDict()
fieldnames = []

with open(file_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        if not row['Website']:  # check whether there is a website
            row.update({'emails': ''})
            row.update({'email_class': ''})
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
                print('Wow! Errors happened!')
                pass
            elif r.status_code < 203:
                while r.status_code != 200:
                    time.sleep(3)
                    r = requests.request('POST', api_url,
                                         headers=headers, json=payload)
                    if r.status_code == 200:
                        break
                resp = r.json()
                row.update({'emails': resp['emails']})
                row.update({'email_class': resp['email_class']})
                pass
            else:
                print('I dunno what this is...', r.status_code)
                pass
        rows.update(row)
    fieldnames = f_csv._fieldnames
    fieldnames.extend(['emails', 'email_class'])

with open(output_file_path,'w') as f:
    f_csv = csv.DictWriter(f, fieldnames)
    f_csv.writeheader()
    f_csv.writerows(rows)
print('ok')