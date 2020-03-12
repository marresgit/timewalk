#!/usr/bin/env python

import requests
import subprocess
import re
from bs4 import BeautifulSoup
import wget
import PyPDF2
import os
from datetime import datetime, date, time

#file that hold the email
import config

todaysDate=date.today()
#url='https://www.coop.se/butiker-erbjudanden/coop/coop-daglivs/'
url='https://www.ica.se/butiker/supermarket/stockholm/ica-supermarket-kungsholmstorg-1227/erbjudanden/'

#get html from coop site
r = requests.get(url)
output = r.text
soup = BeautifulSoup(output, 'html.parser')

regex = re.compile(r'naturgodis', flags=re.IGNORECASE)
if regex.search(output):
    print(f"{todaysDate} - 'DING'")
    subprocess.call("time echo 'Subject:Ica-supermarket DING' | sendmail " + config.email,shell=True)
else:
    print(f"{todaysDate} - ''")



