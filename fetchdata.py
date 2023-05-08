# fetch data from an external API and save it into excel

# dependencies
import os
from time import time
import urllib.request
import pandas as pd
import ssl

# ssl for https request
ssl._create_default_https_context = ssl._create_unverified_context

# calling global excel writer
writer = pd.ExcelWriter('Revison_Blocks_RE_REGION_DATA.xlsx',engine='openpyxl')

# exporting data to excel
def importdata_in_excel (timestamp, FAVC, ACT, AVC, SCHD,region):

    columns = ['Time STamp', 'Forecasting', 'Actual','Available Capacity', 'Schedule']
    
    # Create DataFrame from multiple lists  and saving it   
    df = pd.DataFrame(list(zip(timestamp,FAVC,ACT,AVC,SCHD)), columns = columns)
    df.to_excel(writer,sheet_name=region)
        

# manipulating data
def data_segregation (url_data,region):
    url_content = url_data.split("\\n")

    i = 98
    Block_data = []
    while( i < 194):
        Block_data.append(url_content[i])
        i = i+1
    timestamp = []
    FAVC = []
    ACT = []
    AVC = []
    SCHD = []
    for rev in Block_data :
        Block_content = rev.split(",")
        timestamp.append(Block_content[0])
        FAVC.append(Block_content[1])
        ACT.append(Block_content[2])
        AVC.append(Block_content[3])
        SCHD.append(Block_content[4])

    importdata_in_excel(timestamp,FAVC,ACT,AVC,SCHD,region)


#hitting the fetch API
if os.path.exists('API_LINKS.txt'):
    with open('API_LINKS.txt', 'r') as url:
        for line in url:
            url_line = line.split(",")
            region = url_line[2]
            
            url_data = urllib.request.urlopen(url_line[0]).read().decode('utf-8')
            data_segregation(url_data,region)


#saving gobal writer
writer.save()
print("complete")
