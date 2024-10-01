import zipfile
import os

# Paths
zip_path = '/mnt/data/Data.zip'
extract_path = '/mnt/data/extracted_data'

# Extracting the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print(f"Data extracted to {extract_path}")
