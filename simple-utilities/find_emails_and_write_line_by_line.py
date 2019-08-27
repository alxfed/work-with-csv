"""
take a website name, split it and make an async request, searching
for all the emails in the domain.
"""
import csv
from os import environ
from sys import exit
import time
import json
from tldextract import extract
from collections import OrderedDict
import requests


# constants
file_path = '/media/alxfed/toca/aa-crm/kb-designers/kitchen_and_bath_for_upload.csv'
output_file_path = '/media/alxfed/toca/aa-crm/kb-designers/kitchen_and_bath_done.csv'
line_by_line_write = '/media/alxfed/toca/aa-crm/kb-designers/line_by_line.csv'
credits_check_url = 'https://api.anymailfinder.com/v4.1/account/hits_left.json'
api_url = 'https://api.anymailfinder.com/v4.1/search/company.json'
api_key = environ['API_KEY']
# use this header with all the API calls
headers = {'X-Api-Key': api_key}

# check the number of credits left
r = requests.get(credits_check_url, headers=headers)
if r.status_code==200:
    resp = r.json()
    number = resp['credits_left']
    if number <=100:
        print("Less than 100 credits! I'm not working, sorry!")
        exit()
    else:
        print(number, 'credits left')
else:
    print('The API key is not working.')
    exit()

# initiate the big objects
rows = []
fieldnames = ['Name', 'Type', 'Phone Number', 'Phone Mobile',
              'Phone Voip', 'Phone Toll',
              'Phone Landline', 'Phone Unknown', 'Contact Person',
              'Address', 'City', 'Zipcode', 'State', 'Category',
              'Website', 'Facebook', 'Twitter', 'Google',
              'Linkedin', 'emails', 'email_class']


with open(file_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        website = row['Website']
        if not website:  # check whether there is a website
            row.update({'emails': ''})
            row.update({'email_class': 'no_domain'})
            pass
        else:
            row.update({'emails': ''})
            row.update({'email_class': ''})
            tsd, td, tsu = extract(website)  # tldextract
            payload = {'domain': td + '.' + tsu,
                       'company_name': row['Name']}
            r = requests.post(api_url, headers=headers,
                              json=payload, timeout=60)
            if r.status_code > 202:
                """errors
                """
                if r.status_code == 404:
                    row.update({'email_class': 'not_found'})
                    print(payload, 'not_found')
                elif r.status_code == 451:
                    row.update({'email_class': 'blacklisted'})
                    print(payload, 'blacklisted')
                else:
                    print(payload, r.status_code)
                pass
            elif r.status_code < 203:
                timeout = False
                not_found = False
                attempts = 0
                while r.status_code != 200:
                    time.sleep(3)
                    r = requests.request('POST', api_url,
                                         headers=headers, json=payload)
                    if r.status_code == 200:
                        break
                    elif r.status_code == 404:
                        not_found = True
                        break
                    else:
                        attempts += 1
                        print(attempts, ' - still waiting...')
                        if attempts > 20:
                            timeout = True
                            break
                if not timeout and not not_found:
                    resp = r.json()
                    email_list = resp['emails']
                    row.update({'emails': " ".join(email_list)})
                    row.update({'email_class': resp['email_class']})
                    print(row['Name'], row['emails'], row['email_class'])
                elif timeout:
                    row.update({'email_class': 'timeout'})
                    print(payload, 'Timeout')
                elif not_found:
                    row.update({'email_class': 'not_found'})
                    print(payload, 'Not found')
            else:
                print('I dunno what this is...', r.status_code)
                pass
        rows.append(row)
        with open(line_by_line_write, 'a') as f:
            f_csv = csv.DictWriter(f, fieldnames=fieldnames)
            f_csv.writerow(row)

    # fieldnames = f_csv._fieldnames
    # fieldnames.extend(['emails', 'email_class'])

with open(output_file_path,'w') as f:
    f_csv = csv.DictWriter(f, fieldnames=fieldnames)
    f_csv.writeheader()
    f_csv.writerows(rows)

print('OK')