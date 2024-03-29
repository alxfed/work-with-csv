"""
given: an initial file that was being processed when the processing stopped,
    the resulting file.
needed: the part of the initial file that requires a re-run, the part of the
    resulting file that doesn't require a re-run.
"""
import csv

processed_file_path = '/media/alxfed/toca/aa-crm/int-desanddec/interior_designers_processed.csv'
good_job_path = '/media/alxfed/toca/aa-crm/int-desanddec/interior_designers_with_emails_all.csv'
not_to_redo_path = '/media/alxfed/toca/aa-crm/int-desanddec/not_to_redo.csv'
redo_path = '/media/alxfed/toca/aa-crm/int-desanddec/redo.csv'

# find out what records _do not_ require reprocessing

fieldnames = []
good_job = []
not_to_redo = []
redo = []


with open(processed_file_path, 'r') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        cla = row['email_class']
        if cla == 'verified':
            not_to_redo.append(row)
            good_job.append(row)
        elif cla == 'not_verified':
            not_to_redo.append(row)
            good_job.append(row)
        elif cla == 'not_found':
            not_to_redo.append(row)
        elif cla == 'blacklisted':
            not_to_redo.append(row)
        else:
            redo.append(row)
    fieldnames = f_csv._fieldnames

with open(good_job_path,'w') as f:
    f_csv = csv.DictWriter(f, fieldnames)
    f_csv.writeheader()
    f_csv.writerows(good_job)

with open(not_to_redo_path,'w') as f:
    f_csv = csv.DictWriter(f, fieldnames)
    f_csv.writeheader()
    f_csv.writerows(not_to_redo)

with open(redo_path,'w') as f:
    f_csv = csv.DictWriter(f, fieldnames)
    f_csv.writeheader()
    f_csv.writerows(redo)

