
import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='SaanshaArtworks.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
title ="SaanshaArtworks"
spreadsheet = list(filter(lambda x: x['name'] == title, gc.drive.spreadsheet_metadata()))[0]
sh = gc.open_by_key(spreadsheet['id'])


#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))