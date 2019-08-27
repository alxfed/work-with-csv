"""
given: an initial file that was being processed when the processing stopped,
    the resulting file.
needed: the part of the initial file that requires a re-run, the part of the
    resulting file that doesn't require a re-run.
"""
import csv


initial_file_path = '/media/alxfed/toca/aa-crm/kb-remodelers/kitchen_and_bath_for_upload.csv'
processed_file_path = '/media/alxfed/toca/aa-crm/kb-remodelers/kb_remodelers_with_emails.csv'
good_job_path = '/media/alxfed/toca/aa-crm/kb-remodelers/kitchen_and_bath_remodelers_with_emails.csv'
not_to_redo_path = '/media/alxfed/toca/aa-crm/kb-remodelers/not_to_redo.csv'
redo_file_path = '/media/alxfed/toca/aa-crm/kb-remodelers/kitchen_and_bath_for_redo.csv'

# find out what records _do not_ require reprocessing

fieldnames = []
good_job = []
not_to_redo = []
names_not_to_redo = []
redo = []

with open(processed_file_path, 'r') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        cla = row['email_class']
        if cla == 'verified':
            names_not_to_redo.append(row['Name'])
            not_to_redo.append(row)
            good_job.append(row)
        elif cla == 'not_verified':
            names_not_to_redo.append(row['Name'])
            not_to_redo.append(row)
            good_job.append(row)
        elif cla == 'Not found':
            names_not_to_redo.append(row['Name'])
            not_to_redo.append(row)
        elif cla == 'Blacklisted':
            names_not_to_redo.append(row['Name'])
            not_to_redo.append(row)
    fieldnames = f_csv._fieldnames

with open(good_job_path,'w') as f:
    f_csv = csv.DictWriter(f, fieldnames)
    f_csv.writeheader()
    f_csv.writerows(good_job)

with open(not_to_redo_path,'w') as f:
    f_csv = csv.DictWriter(f, fieldnames)
    f_csv.writeheader()
    f_csv.writerows(not_to_redo)

redo_field_names = []

with open(initial_file_path, 'r') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        if row['Name'] not in names_not_to_redo:
            redo.append(row)
    redo_fieldnames = f_csv._fieldnames

with open(redo_file_path,'w') as f:
    f_csv = csv.DictWriter(f, redo_fieldnames)
    f_csv.writeheader()
    f_csv.writerows(redo)
