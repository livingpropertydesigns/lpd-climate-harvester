import pandas as pd

# Load uszips
zip_df = pd.read_csv("data/raw/uszips.csv", usecols=['zip', 'county_name', 'state_id'])
zip_df = zip_df.rename(columns={'zip': 'ZIP', 'county_name': 'County', 'state_id': 'State'})

# Load ashrae
ashrae_df = pd.read_csv("data/raw/ashrae_county.csv", header=None, dtype=str, skiprows=3, low_memory=False)
ashrae_df = ashrae_df.iloc[:, [0, 1]]
ashrae_df.columns = ['State', 'County']
ashrae_df['State'] = ashrae_df['State'].astype(str).str.upper().str.strip()
ashrae_df['County'] = ashrae_df['County'].astype(str).str.upper().str.replace(' COUNTY', '', regex=False).str.strip()

print("=== Sample from uszips.csv (first 10 rows) ===")
print(zip_df[['ZIP', 'County', 'State']].head(10).to_string(index=False))

print("\n=== Sample from ashrae_county.csv (first 10 rows) ===")
print(ashrae_df.head(10).to_string(index=False))

print("\n=== Looking for Arizona counties ===")
az_zip = zip_df[zip_df['State'] == 'AZ'][['ZIP', 'County']].head(5)
print(az_zip.to_string(index=False))

print("\n=== Does ashrae have 'MARICOPA'? ===")
print(ashrae_df[ashrae_df['County'].str.contains('MARICOPA', na=False)].head(3))