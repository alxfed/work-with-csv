"""
Reading rows of a csv file line by line, doing something with lines,
    writing the resulting line after each transformation.
"""
import csv


input_file_path = '/media/alxfed/toca/aa-crm/preparation/unknown_companies.csv'
input_field_names = ['Name', 'Street Address', 'Company Owner',
                     'Lead Status', 'Phone Landline', 'Phone Mobile',
                     'Phone Toll', 'Phone Unidentified', 'Phone VoIP']
output_file_path = '/media/alxfed/toca/aa-crm/preparation/other_unknown_companies.csv'
output_field_names = ['Name', 'Street Address', 'Company Owner',
                      'Lead Status', 'Phone Landline', 'Phone Mobile',
                      'Phone Toll', 'Phone Unidentified', 'Phone VoIP']


def writeline(filepath, line):
    with open(filepath, 'a') as f:
        f_csv = csv.DictWriter(f, fieldnames=output_field_names)
        f_csv.writerow(line)


rows = []
ind = 0

# initialize the output file
with open(output_file_path,'w') as f:
    f_csv = csv.DictWriter(f, fieldnames=output_field_names)
    f_csv.writeheader()

with open(input_file_path) as f:
    csv_odict = csv.DictReader(f, fieldnames=input_field_names,
                               restkey='rest', restval='')
    _ = next(csv_odict)
    for row in csv_odict:
        # do something with the row
        row.pop('Company Owner', default=None)
        ind += 1
        writeline(output_file_path, row)
        print('ok', ind)