from urllib.request import urlopen
from bs4 import BeautifulSoup
from csv import writer
import re
import time
from datetime import datetime
import pytz
IST = pytz.timezone('Asia/Kolkata')
i=0
i=i+1
u="https://www.amazon.in/Planner-Organiser-Illustrated-Planning-Calendar/dp/B08NZGGKTF/ref=sr_1_3?keywords=the+super+ultra+mega+planner+2022&qid=1640110651&sprefix=super+ultra+mega%2Caps%2C227&sr=8-3"
page = urlopen(u)
soup = BeautifulSoup(page,"html.parser")
title = soup.select('#acrCustomerReviewText , #productDetails_detailBullets_sections1 span span:nth-child(3)')
#title_value = title.string
x=[span.text for span in title]
ratings=int(x[0][:3])
rank=int(re.findall('[0-9]+', x[2])[0])
List=[i,datetime.now(IST),ratings,rank]
with open('Data.csv', 'a',newline='') as f_object:

    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)

    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(List)
    #Close the file object
    f_object.close()
