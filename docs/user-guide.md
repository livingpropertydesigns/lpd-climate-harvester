# User Guide

## Quick Start (Web Version)

1. Go to: [https://lpd-climate-harvester.streamlit.app](https://lpd-climate-harvester.streamlit.app)
2. Enter your 5-digit ZIP code
3. Review the climate data
4. Click **Export CSV for Vectorworks**

## Quick Start (Local Version)

```bash
git clone https://github.com/yourusername/lpd-climate-harvester.git
cd lpd-climate-harvester
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
streamlit run app.py

Output Columns Explained
Column,Description,Source
iecc_zone,IECC Climate Zone + Moisture Regime,eeweather
heating_99,Heating Design Temperature (99%),ASHRAE
cooling_1,Cooling Design Temperature (1%),ASHRAE
data_source,Real / Real (verified) / Fallback,—

Fallback Policy
Some counties have incomplete source data. When this happens, we use verified fallback values and clearly label them in the data_source column.

# Manual J Climate Harvester for Vectorworks

A clean, reliable BIM workflow tool that automates climate data retrieval for **Manual J** residential load calculations directly inside Vectorworks.

### Who This Is For
Primarily built for mid-level Vectorworks-certified draftsmen and architects who want fast, accurate climate data and compliant load calculations without leaving the BIM environment.

---

### Vision
Create a simple, national-scale (USA), easily maintainable system that lets professionals:
- Enter a ZIP code
- Automatically pull accurate climate data (IECC zone, design temperatures, degree days, grains, etc.)
- Generate compliant Manual J loads
- Feed those loads into Manual D duct design worksheets

The goal is **simple, reliable, and BIM-integrated** — no heavy GIS, no manual Excel hunting, just solid, cert-level tools.

---

### Current Status (April 2026)

- ✅ Robust ZIP-to-climate database (33,782 entries)
- ✅ **eeweather** for accurate IECC climate zones (primary source)
- ✅ ASHRAE design temperatures (Heating 99%, Cooling 1%)
- ✅ Clear **Real** vs **Fallback** indicators in output
- ✅ Professional Streamlit UI with real-time lookup
- ✅ One-click CSV export formatted for Vectorworks worksheet import
- ✅ Clean, modular Python architecture

**Note on Data Quality:**  
Some counties use verified fallback values because the source ASHRAE county data is incomplete. These are clearly labeled in the output. The system is stable and production-ready.

---

### Key Features

- ZIP-based climate lookup (IECC zone, design temps, HDD/CDD, grains)
- Clear visual indicators for real vs fallback data
- Basic shading / solar gain reference section
- CSV export ready for Vectorworks
- Professional Streamlit interface
- Easy to maintain and expand

---

### Quick Start

#### 1. Run the Harvester

```bash
python src/main.py
This generates data/processed/manual_j_zip_lookup.csv.
2. Launch the Streamlit UI
Bashstreamlit run app.py
Enter any ZIP code to instantly view:

Climate Zone (IECC)
Heating & Cooling Design Temperatures
Coincident Wet Bulb
Latitude / Longitude
Basic shading guidance
Clear data source label (Real / Fallback)


Using with Vectorworks
## How to Use the Full Workflow (Manual J + Manual S)

1. **Generate Climate Data**
   - Run `python src/main.py` to create `manual_j_zip_lookup.csv`
   - Import it into Vectorworks as a worksheet named **ZIP_Lookup**

2. **Build Your Manual J Worksheet**
   - Use VLOOKUP formulas to pull climate data by ZIP code
   - Complete your building loads (envelope, infiltration, internal gains, etc.)
   - The worksheet will calculate your **Heating Design Load** and **Cooling Design Load**

3. **Create Your Manual S Worksheet**
   - Import `Manual_S_Worksheet_Template.csv` as a new worksheet named **Manual_S**
   - Link it to your Manual J worksheet using VLOOKUP (see template for examples)
   - Enter your equipment selections
   - The worksheet will automatically calculate % oversizing and Pass/Fail status

4. **Review & Document**
   - Use the Pass/Fail columns to verify compliance
   - Export or print the Manual S worksheet for permit submission

This workflow gives you a complete, code-compliant Manual J + Manual S package in one BIM file.

Run the harvester to generate the lookup table.
Import manual_j_zip_lookup.csv into Vectorworks as a new Worksheet named ZIP_Lookup.
Use VLOOKUP formulas in your Manual J worksheet to pull data by ZIP code.

Example:
excel=VLOOKUP($A$1, 'ZIP_Lookup':A:M, 2, FALSE)

Repository Structure
textmanual-j-harvester/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── requirements.txt
├── src/main.py                 # Harvester
├── app.py                      # Streamlit UI
├── data/
│   ├── raw/                    # Source data files
│   └── processed/              # Generated lookup table
└── vectorworks/                # Sample Model

Installation
Bashgit clone https://github.com/livingpropertydesigns/manual-j-harvester.git
cd manual-j-harvester

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

Roadmap

Direct VectorScript / Marionette integration
Expanded shading device calculator
NOAA 1991–2020 normals integration (higher accuracy)
SQLite backend for faster queries
Address / APN-level precision


License
This project is licensed under the MIT License.
You are free to use, modify, and share this tool. Contributions and feedback are welcome.

Built with care for the Vectorworks community.
Teamwork makes the dream work.