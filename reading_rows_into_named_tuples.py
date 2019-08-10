"""
reading rows of csv into (immutable) named tuples
"""
import csv
from collections import namedtuple
import re


file_path = '/media/alxfed/toca/aa-crm/preparation/unknown_companies.csv'

with open(file_path) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    # replace spaces in headers with underscores
    # headers = [header.replace(' ', '_') for header in headers]
    # a full blown version with an imported re is:
    tuple_headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    Row = namedtuple('Row', tuple_headers)
    for r in f_csv:
        row = Row(*r)
        a = row.Name
        b = row.Street_Address