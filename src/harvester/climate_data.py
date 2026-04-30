"""
Climate data processing module (IECC, ASHRAE, ClimDiv).
"""

import pandas as pd
import requests
from pathlib import Path
from io import StringIO

def load_iecc_zones():
    """Load IECC climate zones."""
    print("Loading IECC climate zones...")
    try:
        url = 'https://gist.githubusercontent.com/philngo/d3e251040569dba67942/raw/climate_zones.csv'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        df = pd.read_csv(StringIO(response.text))
        df['FIPS'] = df['County FIPS'].astype(str).str.zfill(5)
        print(f"✓ IECC zones loaded — {len(df)} records.")
        return df
    except Exception as e:
        print(f"Warning: Could not load IECC from Gist ({e}). Using placeholder.")
        return pd.DataFrame(columns=['FIPS', 'Climate Zone (IECC)'])

def load_ashrae_data():
    """Load ASHRAE design temperatures from Tabula export."""
    print("Loading ASHRAE design temperatures...")
    ashrae_path = Path("data/raw/ashrae_county.csv")
    if not ashrae_path.exists():
        print(f"✗ ASHRAE file not found at {ashrae_path}")
        return None
    try:
        df = pd.read_csv(ashrae_path)
        print(f"✓ ASHRAE data loaded — {len(df)} records.")
        print(f"   Columns: {list(df.columns)}")
        return df
    except Exception as e:
        print(f"Warning: ASHRAE load failed ({e}).")
        return None