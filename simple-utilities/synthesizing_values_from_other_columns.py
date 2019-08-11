"""
given: a csv file with a list of objects that have no value of a
    property
needed: a csv file with objects that have this value sythesized from
    the values taken from other columns according to a rule
"""
import csv


read_path = '/media/alxfed/toca/aa-crm/preparation/companies_without_phone.csv'
write_path = '/media/alxfed/toca/aa-crm/preparation/companies_with_added_phone.csv'

fieldnames = []
rows = []

with open(read_path) as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        if row['Phone Landline']:
            row['Phone Number'] = row['Phone Landline']
        if row['Phone Mobile'] and not row['Phone Number']:
            row['Phone Number'] = row['Phone Mobile']
        if row['Phone VoIP'] and not row['Phone Number']:
            row['Phone Number'] = row['Phone VoIP']
        if row['Phone Toll'] and not row['Phone Number']:
            row['Phone Number'] = row['Phone Toll']
        if row['Phone Unidentified'] and not row['Phone Number']:
            row['Phone Number'] = row['Phone Unidentified']
        rows.append(row)
    fieldnames = f_csv._fieldnames

write_headers = fieldnames
write_rows = rows


with open(write_path,'w') as f:
    f_csv = csv.DictWriter(f, write_headers)
    f_csv.writeheader()
    f_csv.writerows(write_rows)
