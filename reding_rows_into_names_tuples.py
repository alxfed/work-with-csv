import csv
from collections import namedtuple


file_path = '/media/alxfed/toca/aa-crm/preparation/unknown_companies.csv'

with open(file_path) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    # replace spaces in headers with underscores
    headers = [header.replace(' ', '_') for header in headers]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        a = row.Name
        b = row.Street_Address