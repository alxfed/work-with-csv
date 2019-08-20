"""
Combine a files with unordered set of lines
and added column of values from another file.
"""

import pandas as pd

origin_file_path = '/media/alxfed/toca/aa-crm/uploads/companies_created.csv'
addition_file_path = '/media/alxfed/toca/aa-crm/uploads/companies_to_create_with_contact_and_emails.csv'
output_file_path = '/media/alxfed/toca/aa-crm/uploads/companies_created_with_emails.csv'

origin = pd.read_csv(origin_file_path)
addition = pd.read_csv(addition_file_path)

def FindEmails(row):
    name = row['Name']
    add = addition.loc[addition['Name'] == name]['emails'].values[0]
    return add


output = origin
output['emails'] = origin.apply(FindEmails, axis=1)
output.to_csv(output_file_path)