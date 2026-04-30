import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

# Page config
st.set_page_config(
    page_title="LPD Climate Harvester",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Logo + Title
col1, col2 = st.columns([1, 6])
with col1:
    try:
        st.image("assets/LPD LOGO.png", width=80)
    except:
        st.write("🌡️")  # Fallback if logo not found

with col2:
    st.title("LPD Climate Harvester")
    st.markdown("**Accurate Climate Data for Vectorworks Manual J**")

st.markdown("---")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/manual_j_zip_lookup.csv")

df = load_data()

@st.cache_data
def load_zip_data():
    return pd.read_csv("data/raw/uszips.csv", usecols=['zip', 'lat', 'lng'])

zip_df = load_zip_data()

# Sidebar
st.sidebar.header("🔍 Lookup by ZIP Code")
zip_input = st.sidebar.text_input("Enter 5-digit ZIP Code", value="86314")

if zip_input:
    try:
        zip_code = int(zip_input)
        zip_match = zip_df[zip_df['zip'] == zip_code]

        if not zip_match.empty:
            lat = zip_match.iloc[0]['lat']
            result = df[df['latitude'] == lat]

            if not result.empty:
                row = result.iloc[0]

                # Main metrics
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Climate Zone (IECC)", row['iecc_zone'])
                    st.metric("Heating DB (99%)", f"{row['heating_99']}°F")
                    st.metric("Cooling DB (1%)", f"{row['cooling_1']}°F")

                with col2:
                    st.metric("Grains Difference", row['grains_diff'])
                    st.metric("HDD (Base 65)", int(row['hdd_base65']))
                    st.metric("CDD (Base 65)", int(row['cdd_base65']))

                with col3:
                    st.metric("Ground Temp Winter", f"{row['ground_winter']}°F")
                    st.metric("Ground Temp Summer", f"{row['ground_summer']}°F")
                    st.metric("Data Source", row.get('data_source', 'Real'))

                # Shading Reference
                st.subheader("Basic Shading Reference")
                shading = pd.DataFrame({
                    "Orientation": ["North", "East", "South", "West"],
                    "Recommended Strategy": [
                        "Minimal shading needed",
                        "Vertical fins + overhang",
                        "Horizontal overhang (2–3 ft)",
                        "Vertical fins + overhang"
                    ]
                })
                st.dataframe(shading, use_container_width=True, hide_index=True)

                # Export
                if st.button("📥 Export CSV for Vectorworks"):
                    csv = result.to_csv(index=False)
                    st.download_button(
                        label="Download CSV",
                        data=csv,
                        file_name=f"LPD_Climate_{zip_code}.csv",
                        mime="text/csv"
                    )
            else:
                st.warning("No climate data found for this ZIP code.")
        else:
            st.error("ZIP code not found in database.")
    except ValueError:
        st.error("Please enter a valid 5-digit ZIP code.")

# Footer
st.markdown("---")
st.caption(f"Built by Living Property Designs, LLC • Last updated: {datetime.now().strftime('%B %d, %Y')} • Data via eeweather + ASHRAE")