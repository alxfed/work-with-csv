"""
given: an initial file that was being processed when the processing stopped,
    the resulting file.
needed: the part of the initial file that requires a re-run, the part of the
    resulting file that doesn't require a re-run.
"""
import csv


initial_file_path = '/media/alxfed/toca/aa-crm/arch-des-employees/architect-designer-employees_rest.csv'
processed_file_path = '/media/alxfed/toca/aa-crm/arch-des-employees/processed_rest_emails.csv'
good_job_path = '/media/alxfed/toca/aa-crm/arch-des-employees/good_job_processed_rest_emails.csv'
not_to_redo_path = '/media/alxfed/toca/aa-crm/arch-des-employees/not_to_redo.csv'
redo_file_path = '/media/alxfed/toca/aa-crm/arch-des-employees/architect-designer-employees_rest_redo.csv'

# find out what records _do not_ require reprocessing

fieldnames = []
good_job = []
not_to_redo = []
contacts_not_to_redo = set()
companies_not_to_redo = set()
redo = []

with open(processed_file_path, 'r') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        cla = row['email_class']
        if cla == 'True':
            contacts_not_to_redo.add(row['Contact ID'])
            not_to_redo.append(row)
            good_job.append(row)
        elif cla == 'False':
            contacts_not_to_redo.add(row['Contact ID'])
            not_to_redo.append(row)
            good_job.append(row)
        elif cla == 'can_not_verify_catch_all':
            companies_not_to_redo.add(row['Associated Company ID'])
            not_to_redo.append(row)
            good_job.append(row)
        elif cla == 'server_not_responding':
            pass
        elif cla == 'unknown':
            pass
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
        if row['Associated Company ID'] not in companies_not_to_redo:
            if row['Contact ID'] not in contacts_not_to_redo:
                redo.append(row)
    redo_fieldnames = f_csv._fieldnames

with open(redo_file_path,'w') as f:
    f_csv = csv.DictWriter(f, redo_fieldnames)
    f_csv.writeheader()
    f_csv.writerows(redo)
