"""
You've bumped into a 'duplicate field name' error, which means that your csv has two columns with 'identical' names.
copy/paste the list of your fields here and find out which of them are duplicates.
"""

tuple_fields = ['Company_ID', 'Last_Modified_Date', 'Lead_Status', 'Total_Revenue',
                'Postal_Code', 'Twitter_Followers', 'Company_Domain_Name',
                'Last_Touch_Converting_Campaign', 'First_Touch_Converting_Campaign',
                'Recent_Deal_Close_Date', 'Number_of_Pageviews', 'Number_of_Employees',
                'Phone_Unidentified', 'Time_of_Last_Session', 'Time_of_First_Visit',
                'Close_Date', 'Facebook_Fans', 'Associated_Deals',
                'Recent_Deal_Amount', 'Number_of_times_contacted',
                'First_Conversion_Date', 'Original_Source_Type',
                'First_Deal_Created_Date', 'Number_of_Form_Submissions',
                'Facebook_Company_Page', 'Create_Date', 'LinkedIn_Bio',
                'First_Conversion', 'City', 'Name', 'Number_of_child_companies',
                'Phone_Toll', 'Number_of_Visits', 'Phone_Number', 'Company_owner',
                'Phone_Landline', 'About_Us', 'Last_Activity_Date', 'Next_Activity_Date',
                'Owner_Assigned_Date', 'State_Region', 'Phone_VoIP', 'Email_address',
                'LinkedIn_Company_Page', 'Total_Money_Raised', 'Phone_Mobile',
                'Associated_Contacts', 'Original_Source_Data__', 'Target_Account',
                'Recent_Conversion_Date', 'Original_Source_Data__', 'Lifecycle_Stage',
                'Last_Contacted', 'Street_Address', 'Recent_Conversion',
                'HubSpot_Team', 'Twitter_Bio', 'Web_Technologies', 'Country',
                'First_Contact_Create_Date', 'Type_Contractor', 'Time_Zone',
                'Time_Last_Seen', 'Time_First_Seen', 'Type', 'Website_URL',
                'Year_Founded', 'Twitter_Handle', 'Google_Plus_Page', 'Days_to_Close',
                'Description', 'Annual_Revenue', 'Parent_Company', 'Industry',
                'Street_Address__', 'Is_Public', 'Associated_Company_ID', 'Associated_Company']

seen = set()
duplicates = []

for name in tuple_fields:
    if name in seen:
        duplicates.append(name)

print(duplicates)
