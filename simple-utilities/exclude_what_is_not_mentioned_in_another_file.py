"""
given: a csv file with a list of objects that belong to entities,
    there is a file with a complete list of entities know to the
    system.
needed: a csv file with objects that belong to known entities,
and: a csv file with objects that belong to _unknown_ entities.
byproduct: a csv file with a list of _new_ (previously unknown)
    entities.
"""
import csv
import re
from collections import namedtuple
import pandas as pd

read_path = '/media/alxfed/toca/aa-crm/preparation/permits_with_general_contractor.csv'
reference_path = '/media/alxfed/toca/aa-crm/preparation/hubspot-crm-exports-all-companies-2019-08-10.csv'
write_path = '/media/alxfed/toca/aa-crm/preparation/permits_with_known_general_contractor.csv'
write_excluded_path = '/media/alxfed/toca/aa-crm/preparation/permits_with_unknown_general_contractor.csv'
write_new_entities = '/media/alxfed/toca/aa-crm/preparation/new_companies.csv'

reference = pd.read_csv(reference_path)
known_entities = reference['Name'].values

rows = []
excluded_rows = []
new_entities_rows = []
new_entities_headers = ['Name', 'Street Address', 'Phone Landline',
                        'Phone Mobile', 'Phone VoIP', 'Phone Toll',
                        'Phone Unidentified', 'Phone Number',
                        'Company owner', 'Lead Status']
seen = set()

with open(read_path) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    tuple_headers = [re.sub('[^a-zA-Z_]', '_', h) for h in headers]
    Row = namedtuple('Row', tuple_headers)
    for r in f_csv:
        row = Row(*r)
        entity = row.CONTRACTOR_GENERAL_CONTRACTOR_Name
        if entity in known_entities:
            rows.append(row)
        else:
            excluded_rows.append(row)
            if not entity in seen:
                seen.add(entity)
                new_entity = {}; phone_number = ''
                new_entity.update({'Name': entity})
                new_entity.update({'Street Address': row.CONTRACTOR_GENERAL_CONTRACTOR_Address})
                if row.CONTRACTOR_GENERAL_CONTRACTOR_Phone_Landline:
                    phone_landline = row.CONTRACTOR_GENERAL_CONTRACTOR_Phone_Landline
                    phone_number = phone_landline
                    new_entity.update({'Phone Landline': phone_landline})
                if row.CONTRACTOR_GENERAL_CONTRACTOR_Phone_Mobile:
                    phone_mobile = row.CONTRACTOR_GENERAL_CONTRACTOR_Phone_Mobile
                    if not phone_number:
                        phone_number = phone_mobile
                    new_entity.update({'Phone Mobile': phone_mobile})
                if row.CONTRACTOR_GENERAL_CONTRACTOR_Phone_Voip:
                    phone_voip = row.CONTRACTOR_GENERAL_CONTRACTOR_Phone_Voip
                    if not phone_number:
                        phone_number = phone_voip
                    new_entity.update({'Phone VoIP': phone_voip})
                if row.CONTRACTOR_GENERAL_CONTRACTOR_Phone_Toll:
                    phone_toll = row.CONTRACTOR_GENERAL_CONTRACTOR_Phone_Toll
                    if not phone_number:
                        phone_number = phone_toll
                    new_entity.update({'Phone Toll': phone_toll})
                if row.CONTRACTOR_GENERAL_CONTRACTOR_Phone_Undinined:
                    phone_unindentified = row.CONTRACTOR_GENERAL_CONTRACTOR_Phone_Undinined
                    if not phone_number:
                        phone_number = phone_unindentified
                    new_entity.update({'Phone Unidentified': phone_unindentified})
                new_entity.update({'Phone Number': phone_number})
                new_entity.update({'Company owner': 'sashadoroshko@marfacabinets.com'})
                new_entity.update({'Lead Status': 'New'})
            new_entities_rows.append(new_entity)

write_headers = headers
write_rows = rows
write_excluded_rows = excluded_rows

with open(write_path,'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(write_headers)
    f_csv.writerows(write_rows)

with open(write_excluded_path,'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(write_headers)
    f_csv.writerows(write_excluded_rows)

with open(write_new_entities,'w') as f:
    f_csv = csv.DictWriter(f, new_entities_headers)
    f_csv.writeheader()
    f_csv.writerows(new_entities_rows)