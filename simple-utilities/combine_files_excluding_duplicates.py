"""
write a list of dictionaries to a csv
"""
import csv

files = ['/media/alxfed/toca/aa-crm/kb-remodelers/kitchen_and_bath_redone.csv',
         '/media/alxfed/toca/aa-crm/kb-remodelers/kitchen_and_bath_remodelers_with_emails.csv']

combined_file_path = '/media/alxfed/toca/aa-crm/kb-remodelers/kitchen_and_bath_remodelers_all.csv'

headers = ['Name', 'Type', 'Phone Number', 'Phone Mobile', 'Phone Voip', 'Phone Toll',
           'Phone Landline', 'Phone Unknown', 'Contact Person',
           'Address', 'City', 'Zipcode', 'State', 'Category',
           'Website', 'Facebook', 'Twitter', 'Google',
           'Linkedin', 'emails', 'email_class']
good = ['verified', 'not_verified']
seen = set()
output_rows = []

for file in files:
    with open(file) as f:
        f_csv = csv.DictReader(f, restkey='Rest', restval='')
        for row in f_csv:
            if row['email_class'] in good:
                if row['Name'] not in seen:
                    output_rows.append(row)
                    seen.add(row['Name'])
            else:
                pass

print('scanned, ready to write')

with open(combined_file_path,'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(output_rows)