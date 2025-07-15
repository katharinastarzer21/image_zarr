from urllib.request import urlretrieve
import os
import sys

def download_data(var):
    print(var)
    url = f"https://public.hub.geosphere.at/datahub/resources/spartacus-v2-1d-1km/filelisting/SPARTACUS2-DAILY_{var}_2025.nc"
    filename = os.path.basename(url)
    base = "/tmp"
    urlretrieve(url, os.path.join(base,filename))
    
                              
if __name__ == "__main__":
    var = sys.argv[1]
    download_data(var)