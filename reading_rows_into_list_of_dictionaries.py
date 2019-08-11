"""
Reading rows of a csv file into a (mutable) sequence/list of dictionaries
"""
import csv


file_path = '/media/alxfed/toca/aa-crm/preparation/unknown_companies.csv'
fieldnames = []

with open(file_path) as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        a = row['Name']
        b = row['Street Address']
    fieldnames = f_csv._fieldnames  # after reading all the rows it borrows this
                                    # 'protected field' from the object. Otherwise
                                    # it is unclear how to set the headers for writing.