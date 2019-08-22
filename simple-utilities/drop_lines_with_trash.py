"""
given: a csv file with a list of objects that may have a value of the
    property meaning that it is trash
needed: a csv file with these lines dropped
"""
import csv


read_path = '/media/alxfed/toca/aa-crm/enrich/kitchen_and_bath_unprocessed.csv'
write_path = '/media/alxfed/toca/aa-crm/enrich/kitchen_and_bath.csv'

trash_list = ['houzz', 'yelp', 'lowes', 'homedepot']

fieldnames = []
rows = []
seen = set()
duplicates = []

def NotTrash(text, trash_list):
    for trash in trash_list:
        if trash in text:
            return None
    return text

with open(read_path) as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        if NotTrash(row['Website'], trash_list):
            rows.append(row)
    fieldnames = f_csv._fieldnames


write_headers = fieldnames
write_rows = rows


with open(write_path,'w') as f:
    f_csv = csv.DictWriter(f, write_headers)
    f_csv.writeheader()
    f_csv.writerows(write_rows)
