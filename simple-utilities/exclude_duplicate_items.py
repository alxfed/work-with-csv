"""
given: a csv file with a list of objects that have no value of a
    property
needed: a csv file with objects that have this value sythesized from
    the values taken from other columns according to a rule
"""
import csv


read_path = '/media/alxfed/toca/aa-crm/enrich/kitchen_and_bath_designers_with_websites_and_added_phone.csv'
write_path = '/media/alxfed/toca/aa-crm/enrich/kitchen_and_bath_designers_no_duplicates.csv'

fieldnames = []
rows = []
seen = set()
duplicates = []

with open(read_path) as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        if row['Name'] in seen:
            duplicates.append(row['Name'])
        else:
            seen.add(row['Name'])
            rows.append(row)
    fieldnames = f_csv._fieldnames

print('Duplicates: ', len(duplicates))
write_headers = fieldnames
write_rows = rows


with open(write_path,'w') as f:
    f_csv = csv.DictWriter(f, write_headers)
    f_csv.writeheader()
    f_csv.writerows(write_rows)
