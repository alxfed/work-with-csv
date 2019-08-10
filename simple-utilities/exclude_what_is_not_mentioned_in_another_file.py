"""
given: a csv file with a list of objects that belong to entities,
    there is a file with a complete list of entities know to the
    system.
needed: a csv file with objects that belong to known entities,
and: a csv file with objects that belong to _unknown_ entities.
byproduct: a csv file with a list of _new_ (previously unknown)
    entities.
"""
import csv
import re
from collections import namedtuple

read_path = '/media/alxfed/toca/aa-crm/preparation/permits-09-08-2019_10_54_27.csv'
reference_path = '/media/alxfed/toca/aa-crm/preparation/hubspot-crm-exports-all-companies-2019-08-10.csv'
write_path = '/media/alxfed/toca/aa-crm/preparation/permits_with_known_general_contractor.csv'
write_excluded_path = '/media/alxfed/toca/aa-crm/preparation/permits_with_unknown_general_contractor.csv'
write_new_entities = '/media/alxfed/toca/aa-crm/preparation/new_companies.csv'

rows = []
excluded_rows = []
new_entities_rows =[]

with open(read_path) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    tuple_headers = [re.sub('[^a-zA-Z_]', '_', h) for h in headers]
    Row = namedtuple('Row', tuple_headers)
    for r in f_csv:
        row = Row(*r)
        if not row.CONTRACTOR_GENERAL_CONTRACTOR_Name:
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