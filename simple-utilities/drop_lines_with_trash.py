"""
given: a csv file with a list of objects that may have a value of the
    property meaning that it is trash. Some lines can have it missing
    altogether, they should be dumped too.
needed: a csv file with these lines dropped
"""
import csv
from tldextract import extract


read_path = '/media/alxfed/toca/aa-crm/kb-remodelers/kitchen_and_bath_processed.csv'
write_path = '/media/alxfed/toca/aa-crm/kb-remodelers/kitchen_and_bath_final.csv'
leftowers_path = '/media/alxfed/toca/aa-crm/kb-remodelers/kitchen_and_bath_leftowers.csv'


trash_list = ['houzz', 'yelp', 'yahoo', 'lowes', 'homedepot', 'facebook',
              'blogspot', 'wix', 'smithe', 'sbcglobal', 'ymail',
              'mac', 'twitter', 'aol', 'linkedin', 'google', 'gmail',
              'artvan', 'nu-tub', 'https', 'icloud', 'me.com', 'fb.me',
              'tinyurl', 'vpweb', 'weebly', 'rebath', 'bathfitter']

fieldnames = []
rows = []
lrows = []
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
        if row['Name'] in seen:
            lrows.append(row)
        else:
            if row['Website']:
                if NotTrash(row['Website'], trash_list):
                    tsd, td, tsu = extract(row['Website'])  # tldextract
                    domain_name = td + '.' + tsu
                    row['Website'] = domain_name
                    rows.append(row)
                    seen.add(row['Name'])
                else:
                    lrows.append(row)
            else:
                lrows.append(row)
    fieldnames = f_csv._fieldnames


write_headers = fieldnames
write_rows = rows
leftower_rows = lrows


with open(write_path,'w') as f:
    f_csv = csv.DictWriter(f, write_headers)
    f_csv.writeheader()
    f_csv.writerows(write_rows)

with open(leftowers_path,'w') as f:
    f_csv = csv.DictWriter(f, write_headers)
    f_csv.writeheader()
    f_csv.writerows(leftower_rows)

