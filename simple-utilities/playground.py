import csv
from os import environ
from sys import exit
import time
from tldextract import extract
from collections import OrderedDict
import requests
from email.utils import parseaddr


email = 'alex.fedotov@aol.com'

name = email.split('@')[0]

print('ok')