"""
given: a csv file with a list of objects that have no value of a
    property
needed: a csv file with objects that have this value sythesized from
    the values taken from other columns according to a rule
"""
import csv


read_path = '/media/alxfed/toca/aa-crm/kb-remodelers/upload/kitchen_and_bath_remodelers_all.csv'
write_path = '/media/alxfed/toca/aa-crm/kb-remodelers/upload/kitchen_and_bath_remodelers_with_emails_all_ready.csv'

fieldnames = []
rows = []

with open(read_path) as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        if row['Phone Landline']:
            row['Phone Number'] = row['Phone Landline']
        if row['Phone Mobile'] and not row['Phone Number']:
            row['Phone Number'] = row['Phone Mobile']
        if row['Phone Voip'] and not row['Phone Number']:
            row['Phone Number'] = row['Phone Voip']
        if row['Phone Toll'] and not row['Phone Number']:
            row['Phone Number'] = row['Phone Toll']
        if row['Phone Unknown'] and not row['Phone Number']:
            row['Phone Number'] = row['Phone Unknown']
        row['Name'] = row['Name'].title()
        rows.append(row)
    fieldnames = f_csv._fieldnames

write_headers = fieldnames
write_rows = rows


with open(write_path,'w') as f:
    f_csv = csv.DictWriter(f, write_headers)
    f_csv.writeheader()
    f_csv.writerows(write_rows)
