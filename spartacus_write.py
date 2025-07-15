import xarray as xr
import numpy as np
import zarr
import os
import sys

def write_data(var):
    year = 2025
    fill_value = -999
    artifact_path = f"/tmp/SPARTACUS2-DAILY_{var}_{year}.nc"
    zarr_path = "/eodc/private/tempearth/SPARTACUS.zarr"
   

    # NetCDF öffnen
    ds_nc = xr.open_dataset(artifact_path, mask_and_scale=False).load()

    store = zarr.storage.LocalStore(zarr_path)
    group = zarr.group(store=store)  
    zarr.consolidate_metadata(store)

    print(group['TX'])

   
    data = ds_nc[var].values.astype("float32")
    data[data == fill_value] = np.nan
    data_filled = np.where(np.isnan(data), fill_value, data).astype("int16")

    
    ref_date = np.datetime64("1961-01-01")
    start_date = np.datetime64(f"{year}-01-01")
    start_idx = int((start_date - ref_date) / np.timedelta64(1, "D"))
    num_days = data.shape[0]
    end_idx = start_idx + num_days

    group[var][start_idx:end_idx, :, :] = data_filled
    print(f"✅ {var} für {year} eingefügt: [{start_idx}:{end_idx}]")
    
if __name__=="__main__":
    var = sys.argv[1]
    write_data(var)
    

    