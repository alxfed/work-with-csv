import csv
from collections import namedtuple


file_path = '/media/alxfed/toca/aa-crm/preparation/unknown_companies.csv'

with open(file_path) as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    # replace spaces in headings with underscores
    headings = [heading.replace(' ', '_') for heading in headings]
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        a = row.Name
        b = row.Street_Address