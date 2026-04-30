"""
Core module for building the ZIP climate lookup table.
"""

import pandas as pd
import requests
import io
from pathlib import Path

def build_zip_lookup() -> pd.DataFrame:
    """Main function to build the complete ZIP lookup table using proven logic."""
    print("Loading ZIP data...")

    zip_path = Path("data/raw/uszips.csv")
    if not zip_path.exists():
        print(f"✗ Error: Could not find {zip_path}")
        print("   Please make sure uszips.csv is in the data/raw/ folder.")
        return None

    try:
        zip_df = pd.read_csv(zip_path, usecols=['zip', 'county_name', 'lat', 'lng', 'city', 'state_id'])
        zip_df = zip_df.rename(columns={
            'zip': 'ZIP',
            'county_name': 'County',
            'lat': 'Latitude',
            'lng': 'Longitude',
            'city': 'City',
            'state_id': 'State_Abbr'
        })
        zip_df = zip_df[zip_df['County'].notna() & zip_df['State_Abbr'].notna()]
        print(f"✓ ZIP data loaded — {len(zip_df):,} records.")
    except Exception as e:
        print(f"✗ Error loading uszips.csv: {e}")
        return None

    # FIPS mapping (proven logic from original script)
    print("Building FIPS mappings...")
    try:
        fips_url = 'https://www2.census.gov/geo/docs/reference/codes/files/national_county.txt'
        response = requests.get(fips_url, timeout=10)
        fips_txt = io.StringIO(response.text)
        fips_df = pd.read_csv(fips_txt, sep=',', header=None, names=['State_Abbr', 'FIPS_State', 'FIPS_County', 'County_Name', 'LSAD'])
        fips_df = fips_df.iloc[1:].reset_index(drop=True).dropna()
        fips_df['County_Name'] = fips_df['County_Name'].astype(str).str.strip()
        fips_df['State_Abbr'] = fips_df['State_Abbr'].astype(str).str.strip()
        fips_df['FIPS'] = fips_df['FIPS_State'].astype(str).str.zfill(2) + fips_df['FIPS_County'].astype(str).str.zfill(3)
        fips_df['County_Key'] = fips_df['County_Name'].str.replace(' County', '', regex=False).str.strip() + ' ' + fips_df['State_Abbr']
        fips_dict = dict(zip(fips_df['County_Key'], fips_df['FIPS']))
    except Exception as e:
        print(f"Warning: FIPS fetch failed ({e}).")
        fips_dict = {}

    # Map FIPS to ZIP DataFrame
    zip_df['County_Key'] = zip_df['County'].str.replace(' County', '', regex=False).str.strip() + ' ' + zip_df['State_Abbr'].str.strip()
    zip_df['FIPS'] = zip_df['County_Key'].map(fips_dict)

    print(f"FIPS mapping complete. Matched {zip_df['FIPS'].notna().sum():,} records.")

    return zip_df