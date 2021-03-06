
# coding: utf-8

# In[1]:

import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
document_key = "13bsf7rP9ubfBSX7-hK3QayZIaUkTxrXaOZqGsfLjWX4"
credentials = ServiceAccountCredentials.from_json_keyfile_name('../../../../../SheetsBot-32718db5596a.json', scope)
csvfile = "output.csv"
gc = gspread.authorize(credentials)
wks = gc.open_by_key(document_key)
worksheet = wks.worksheet("Form Responses 1")
list_of_lists = worksheet.get_all_values()
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(list_of_lists)

import pandas as pd
output = pd.read_csv(csvfile)
output[:3]


# In[ ]:




# In[ ]:



