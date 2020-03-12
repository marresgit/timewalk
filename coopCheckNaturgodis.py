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
url='https://www.coop.se/butiker-erbjudanden/coop/coop-daglivs/'

#get html from coop site
r = requests.get(url)
output = r.text
soup = BeautifulSoup(output, 'html.parser')

#loop through and parse the veckoblad
for a in soup.find_all('a', attrs={'class':'Button Button--green Button--radius u-marginTmd'}, href=True):
    PDF = a['href']

#print(PDF)

if os.path.isfile('download.wget'):
    print("File already exists")
else:
    filename = wget.download(PDF)

#creating an object
file = open('download.wget', 'rb')

regex = re.compile(r'naturgodis', flags=re.IGNORECASE)
#creating a pdf reader object
ding = ""
fileReader = PyPDF2.PdfFileReader(file)
for count in range(0,fileReader.getNumPages()):
    getPages = fileReader.getPage(count)
    getPdfText = getPages.extractText()
    #print(getPdfText)
    if regex.search(getPdfText):
        ding = "True"
if ding == "True":
    print(f"{todaysDate} - 'DING'")
    subprocess.call("time echo 'Subject:Coop DING' | sendmail " + config.email,shell=True)
else:
    print(f"{todaysDate} - ''")


 
os.remove("download.wget")

