"""
Reading rows of a csv file into a list of ordered dictionaries (for 3.6+),
    then writing it into a duplicate file.
"""
import csv


input_file_path = '/media/alxfed/toca/aa-crm/preparation/unknown_companies.csv'
output_file_path = '/media/alxfed/toca/aa-crm/preparation/other_unknown_companies.csv'

fieldnames = []
rows = []

with open(input_file_path) as f:
    csv_odict = csv.DictReader(f, restkey='Rest', restval='')
    for row in csv_odict:
        rows.append(row)
    fieldnames = csv_odict._fieldnames  # after reading all the rows it borrows this
                                        # 'protected field' from the object. Otherwise
                                        # it is unclear how to set the (mandatory) headers for writing.

with open(output_file_path,'w') as f:
    f_csv = csv.DictWriter(f, fieldnames=fieldnames)
    f_csv.writeheader()
    f_csv.writerows(rows)