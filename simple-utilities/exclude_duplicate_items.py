"""
given: a csv file with a list of objects that have no value of a
    property
needed: a csv file with objects that have this value sythesized from
    the values taken from other columns according to a rule
"""
import csv


read_path = '/home/alxfed/Downloads/houzz_companies-19-08-2019_13_28_57.csv'
write_path = '/home/alxfed/Downloads/houzz_companies-19-08-2019_13_28_57_no_duplicates.csv'

fieldnames = []
rows = []
seen = set()
duplicates = []

with open(read_path) as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        if row['Name'] in seen:
            duplicates.append(row['Name'])
        else:
            seen.add(row['Name'])
            rows.append(row)
    fieldnames = f_csv._fieldnames

print('Duplicates: ', len(duplicates))
write_headers = fieldnames
write_rows = rows


with open(write_path,'w') as f:
    f_csv = csv.DictWriter(f, write_headers)
    f_csv.writeheader()
    f_csv.writerows(write_rows)
