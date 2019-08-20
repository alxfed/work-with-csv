import csv
from os import environ
from sys import exit
import time
from tldextract import extract
from collections import OrderedDict
import requests
from email.utils import parseaddr


email = 'alex.fedotov@aol.com'

left_side, right_side = email.split('@')
name, surname = left_side.split('.')

print('ok')