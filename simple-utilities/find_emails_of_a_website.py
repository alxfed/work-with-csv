"""
take a website name, split it and make an async request, searching
for all the emails in the domain.
"""
import csv
import os
from tldextract import extract

api_key = os.environ['API_KEY']

print('ok')