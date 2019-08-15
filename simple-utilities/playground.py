import csv
from os import environ
from sys import exit
import time
from tldextract import extract
from collections import OrderedDict
import requests


# constants
file_path = '/media/alxfed/toca/aa-crm/other-lists/arcs_interor_test.csv'
output_file_path = '/media/alxfed/toca/aa-crm/other-lists/archs_with_emails_test.csv'

# imitation
emails = ['alxfed@gmail.com', 'votodef.xela@gmail.com', 'alxfed.robot@gmail.com']

# initiate the big objects
rows = []
fieldnames = ['Name', 'Phone Mobile', 'Phone Voip', 'Phone Toll',
              'Phone Landline', 'Phone Unknown', 'Contact Person',
              'Address', 'City', 'Zipcode', 'State', 'Category',
              'Website', 'Facebook', 'Twitter', 'Google',
              'Linkedin', 'emails', 'email_class']


with open(file_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        website = row['Website']
        row.update({'emails': " ".join(emails)})
        row.update({'email_class': 'verified'})
        print(row['Name'], row['emails'], row['email_class'])
        rows.append(row)
    # fieldnames = f_csv._fieldnames
    # fieldnames.extend(['emails', 'email_class'])

with open(output_file_path,'w') as f:
    f_csv = csv.DictWriter(f, fieldnames=fieldnames)
    f_csv.writeheader()
    f_csv.writerows(rows)

print('It looks like everything worked. OK.')