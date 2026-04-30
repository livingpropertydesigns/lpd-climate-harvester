"""
LPD Climate Harvester - Streamlit App
Single-row CSV export (preserves exact column order)
"""

import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="LPD Climate Harvester", page_icon="🌡️", layout="wide")

st.title("🌡️ LPD Climate Harvester")
st.caption("Living Property Designs, LLC  •  Accurate Manual J Climate Data for Vectorworks")

@st.cache_data(show_spinner="Loading climate database...")
def load_data():
    csv_path = Path("data/processed/manual_j_zip_lookup.csv")
    if not csv_path.exists():
        st.error("Run `python src/main.py` first to generate the data.")
        st.stop()
    return pd.read_csv(csv_path)

df = load_data()

st.sidebar.header("🔍 ZIP Code Lookup")
zip_input = st.sidebar.text_input("Enter 5-digit ZIP Code", value="86303", max_chars=5)

if zip_input.strip().isdigit():
    zip_int = int(zip_input.strip())
    matched = df[df['ZIP'] == zip_int]
    
    if not matched.empty:
        row = matched.iloc[0]
        st.sidebar.success(f"✓ Found: {row['city']}")
        
        st.subheader(f"Results for ZIP {zip_int} — {row['city']}")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("IECC Climate Zone", str(row['iecc_zone']))
        col2.metric("Heating 99%", f"{row['heating_99']}°F")
        col3.metric("Cooling 1%", f"{row['cooling_1']}°F")
        col4.metric("Data Source", str(row['data_source']))
        
        st.divider()
        
        # Download ONLY this one row
        csv_data = matched.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV for Vectorworks (this ZIP only)",
            data=csv_data,
            file_name=f"manual_j_{zip_int}.csv",
            mime="text/csv",
            help="Tiny file with headers + 1 row — ready for Vectorworks import"
        )
    else:
        st.error(f"ZIP {zip_int} not found in database.")
else:
    st.info("Enter a valid 5-digit ZIP code in the sidebar.")

st.caption("Data: NOAA + ASHRAE + eeweather  •  33 columns preserved  •  April 2026")