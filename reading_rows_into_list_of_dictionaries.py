"""
Reading rows of a csv file into a (mutable) sequence/list of dictionaries
"""
import csv


file_path = '/media/alxfed/toca/aa-crm/preparation/unknown_companies.csv'

with open(file_path) as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        a = row['Name']
        b = row['Street Address']