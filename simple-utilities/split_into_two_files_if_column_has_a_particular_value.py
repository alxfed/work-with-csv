"""
given: a csv file with empty cells in a column with mandatory parameter;
needed: a csv file _without_ the lines with missing parameter;
byproduct: a csv file with the excluded lines.
"""
import csv
import re
from collections import namedtuple

read_path = '/media/alxfed/toca/aa-crm/arch-des-employees/architect-designer-employees.csv'
'''
headers = ['Contact ID', 'First Name', 'Last Name', 'Broadcast Clicks',
           'Time registration email was sent', 'Last marketing email name',
           'Status', 'Registered At', 'Marketing emails opened',
           'Lead Status', 'Total Revenue', 'Gender', 'Postal Code',
           'Last Contract Viewed Date', 'Klout Score', 'IP City',
           'Company size', 'Last Touch Converting Campaign',
           'First Touch Converting Campaign', 'Recent Deal Close Date',
           'Number of Pageviews', 'Legal basis for processing contacts data',
           'Became a Marketing Qualified Lead Date', 'Military status',
           'Last Meeting Booked Campaign', 'Time of Last Visit',
           'Time of First Visit', 'Facebook Clicks', 'Close Date',
           'Do you have a showroom? ', 'Field of study', 'Message',
           'HelloSign Meta 30', 'Associated Deals', 'HelloSign Meta 1',
           'Recent Deal Amount', 'Opted out of email: Marketing Information',
           'HelloSign Meta 20', 'Do you have a dedicated kitchen designer? ',
           'Number of times contacted', 'Number of Sales Activities',
           'Google Plus Clicks', 'HelloSign Meta 2', 'First Conversion Date',
           'Date of birth', 'Recent Sales Email Clicked Date',
           'Recent Sales Email Opened Date', 'Original Source',
           'HelloSign Meta 21', 'HelloSign Meta 3', 'Email Two',
           'First Deal Created Date', 'HelloSign Meta 10',
           'Number of Form Submissions', 'HelloSign Meta 22',
           'Opted out of email: One to One', 'Currently in workflow',
           'HelloSign Meta 4', 'Last Meeting Booked Medium',
           'Most Recent Social Click', 'Create Date', 'LinkedIn Bio',
           'First Conversion', 'Became a Sales Qualified Lead Date',
           'Last Meeting Booked', 'HelloSign Meta 11', 'HelloSign Meta 23',
           'First marketing email click date', 'HelloSign Meta 5',
           'City', 'Start date', 'How did you hear about Marfa Cabinets Inc? ',
           'HelloSign Meta 12', 'Preferred language', 'HelloSign Meta 24',
           'HelloSign Meta 6', 'Mobile Phone Number',
           'Number of event completions', 'Degree', 'HelloSign Meta 13',
           'HelloSign Meta 25', 'Average Pageviews',
           'Marketing emails delivered', 'HelloSign Meta 7',
           'Number of Unique Forms Submitted', 'Email Confirmed',
           'Last Modified Date', 'HelloSign Meta 14', 'HelloSign Meta 26',
           'Number of Visits', 'Work email', 'IP Country Code',
           'HelloSign Meta 8', 'Phone Number', 'Became a Subscriber Date',
           'LinkedIn Clicks', 'HelloSign Meta 15', 'HelloSign Meta 27',
           'HelloSign Meta 9', 'Marketing email confirmation status',
           'Contact owner', 'External ID', 'Event Revenue', 'HelloSign Meta 16',
           'HelloSign Meta 28', 'Last Activity Date', 'Next Activity Date',
           'HelloSign CC', 'Last Meeting Booked Source', 'Owner Assigned Date',
           'HelloSign Meta 17', 'HelloSign Meta 29', 'State/Region',
           'Became an Opportunity Date', 'Marketing emails clicked',
           'Follower Count', 'Last marketing email open date',
           'HelloSign Meta 18', 'Opted out of email: Architects & Designers',
           'Unsubscribed from all email', 'Membership Notes',
           'HelloSign Meta 19', 'Last Page Seen', 'First Page Seen',
           'Original Source Drill-Down 1', 'Last marketing email send date',
           'IP State Code/Region Code', 'Recent Conversion Date',
           'Became an Other Lifecycle Date', 'Dealer Registration Comments',
           'Original Source Drill-Down 2', 'Lifecycle Stage', 'School',
           'Last Contacted', 'Street Address', 'Recent Conversion',
           'HubSpot Team', 'Twitter Bio', 'Twitter Clicks', 'Not interested',
           'When would you like to visit our showroom?',
           'What other brands of kitchen cabinetry do you currently offer?',
           'Country', 'LinkedIn Connections', 'Last marketing email click date',
           'Persona', 'Salutation', 'Sends Since Last Engagement',
           'Became a Customer Date', 'Currently in Sequence', 'IP State/Region',
           'Relationship Status', 'Time Last Seen', 'Time First Seen',
           'Job function', 'Became a Lead Date', 'Recent Sales Email Replied Date',
           'What design software do you use?', 'Last Contract Signed Date',
           'Website URL', 'Job Title', 'Email Domain', 'HubSpot Score',
           'Twitter Username', 'First Referring Site', 'Last Referring Site',
           'Twitter Profile Photo', 'Became an Evangelist Date', 'Days To Close',
           'Email', 'Company Name', 'Annual Revenue', 'Marital Status',
           'First marketing email open date', 'IP Timezone', 'Fax Number',
           'Pending Signature', 'IP Country', 'Seniority', 'Industry',
           'Domain to which registration email was sent',
           'First marketing email send date', 'Email Address Quarantined',
           'Graduation date', 'Number of Employees', 'Marketing emails bounced',
           'Associated Company ID', 'Associated Company']
'''
write_path = '/media/alxfed/toca/aa-crm/arch-des-employees/architect-designer-employees_info.csv'
write_excluded_path = '/media/alxfed/toca/aa-crm/arch-des-employees/architect-designer-employees_rest.csv'

rows = []
excluded_rows = []

with open(read_path) as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        name = row['First Name'].lower()
        if name.startswith('info'):
            rows.append(row)
        else:
            excluded_rows.append(row)
    fieldnames = f_csv._fieldnames


write_headers = fieldnames
write_rows = rows
leftower_rows = excluded_rows


with open(write_path,'w') as f:
    f_csv = csv.DictWriter(f, write_headers)
    f_csv.writeheader()
    f_csv.writerows(write_rows)

with open(write_excluded_path,'w') as f:
    f_csv = csv.DictWriter(f, write_headers)
    f_csv.writeheader()
    f_csv.writerows(leftower_rows)
