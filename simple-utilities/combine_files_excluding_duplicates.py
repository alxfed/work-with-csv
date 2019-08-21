"""
write a list of dictionaries to a csv
"""
import csv

files = ['/media/alxfed/toca/aa-crm/enrich/sheet0_agents.csv',
         '/media/alxfed/toca/aa-crm/enrich/sag_agents.csv',
         '/media/alxfed/toca/aa-crm/enrich/lag_agents.csv']

combined_file_path = '/media/alxfed/toca/aa-crm/enrich/all_agents.csv'

headers = ['Agent Name', 'Agent ID', 'Agent Phone', 'Agent Email']
seen = set()
output_rows = []

for file in files:
    with open(file) as f:
        f_csv = csv.DictReader(f, restkey='Rest', restval='')
        for row in f_csv:
            if row['Agent ID'] not in seen:
                output_rows.append(row)
                seen.add(row['Agent ID'])
            else:
                print('seen')

print('scanned, ready to write')

with open(combined_file_path,'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(output_rows)