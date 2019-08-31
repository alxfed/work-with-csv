"""
given: a csv file with a list of objects that belong to entities,
    there is a file with a complete list of entities known to the
    system.
needed: a csv file with objects that belong to _unknown_ entities.
byproduct: a csv file with a list of _new_ (previously unknown)
    entities.
"""
import csv
import re
from collections import namedtuple
import pandas as pd
import os


read_path = '/media/alxfed/toca/aa-crm/uploads/interior_designers_with_emails_and_added_phone.csv'
reference_path = '/media/alxfed/toca/aa-crm/uploads/hubspot-crm-exports-all-companies-2019-08-31-1.csv'
# write_path = '/media/alxfed/toca/aa-crm/uploads/new-companies.csv'
write_excluded_path = '/media/alxfed/toca/aa-crm/uploads/known-companies.csv'
write_new_entities = '/media/alxfed/toca/aa-crm/uploads/new_companies.csv'

reference = pd.read_csv(reference_path)
known_entities = reference['Name'].values

rows = []
excluded_rows = []
new_entities_rows = []
headers = ['Name', 'Type', 'Category', 'Phone Number', 'Phone Contact',
           'Phone Mobile', 'Phone Voip', 'Phone Toll', 'Phone Landline',
           'Phone Unknown', 'Address', 'City', 'State', 'Zipcode',
           'Linkedin', 'Facebook', 'Twitter', 'Website',
           'emails', 'email_class']

seen = set()

with open(read_path) as f:
    f_csv = csv.DictReader(f, restkey='Rest', restval='')
    for row in f_csv:
        entity = row['Name']
        if entity not in known_entities:
            new_entities_rows.append(row)
        else:
            excluded_rows.append(row)

write_headers = headers
write_rows = rows
write_excluded_rows = excluded_rows

'''
with open(write_path,'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(write_headers)
    f_csv.writerows(write_rows)
'''

with open(write_excluded_path,'w') as f:
    f_csv = csv.DictWriter(f, write_headers)
    f_csv.writeheader()
    f_csv.writerows(write_excluded_rows)

with open(write_new_entities,'w') as f:
    f_csv = csv.DictWriter(f, write_headers)
    f_csv.writeheader()
    f_csv.writerows(new_entities_rows)