from urllib.request import urlretrieve
import os
import sys
import datetime

def download_data(var):
    
    today = datetime.date.today()- datetime.timedelta(days=3)
    year = today.strftime('%Y')
    url = f"https://public.hub.geosphere.at/datahub/resources/spartacus-v2-1d-1km/filelisting/{var}/SPARTACUS2-DAILY_{var}_{year}.nc"
    filename = os.path.basename(url)
    base = "/tmp"
    urlretrieve(url, os.path.join(base,filename))
    
                              
if __name__ == "__main__":
    var = sys.argv[1]
    download_data(var)
