import requests
import pandas as pd
import configparser
config=configparser.ConfigParser()
config.read(r'config.ini')
data=pd.read_csv(str(config['parameter']['file_to_read']))
for i in range(0,len(data),1):
    k=data.iloc[i][0]
    end_point = k
    res=requests.post(str(config['parameter']['api_address']),data=end_point)
    with open(str(config['parameter']['file_to_save']),'a') as f:
        f.writelines(res.text)
        f.write("\n")
