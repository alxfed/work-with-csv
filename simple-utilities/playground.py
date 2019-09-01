"""
pandas formatting during parsing:
https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
"""


import csv
import pandas as pd


file_path = '/media/alxfed/toca/aa-crm/file/companies.csv'

companies = pd.read_csv(file_path)


print('ok')