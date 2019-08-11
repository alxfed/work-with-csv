"""
given: a csv file with empty cells in a column with mandatory parameter;
needed: a csv file _without_ the lines with missing parameter;
byproduct: a csv file with the excluded lines.
"""
import csv
import re
from collections import namedtuple

read_path = '/media/alxfed/toca/aa-crm/preparation/companies_with_added_phone.csv'
write_path = '/media/alxfed/toca/aa-crm/preparation/companies_to_update.csv'
write_excluded_path = '/media/alxfed/toca/aa-crm/preparation/companies_hopeless.csv'

rows = []
excluded_rows = []

with open(read_path) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    tuple_headers = [re.sub('[^a-zA-Z_]', '_', h) for h in headers]
    Row = namedtuple('Row', tuple_headers)
    for r in f_csv:
        row = Row(*r)
        if not row.Phone_Number:
            excluded_rows.append(row)
        else:
            rows.append(row)

write_headers = headers
write_rows = rows
write_exclued_rows = excluded_rows

with open(write_path,'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(write_headers)
    f_csv.writerows(write_rows)

with open(write_excluded_path,'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(write_headers)
    f_csv.writerows(write_exclued_rows)