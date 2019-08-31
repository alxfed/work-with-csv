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
    tuple_headers = [re.sub('[^a-zA-Z_]', '_', h) for header in headers]
    Row = namedtuple('Row', tuple_headers)
    for r in f_csv:
        row = Row(*r)
        a = row.Name
        b = row.Street_Address