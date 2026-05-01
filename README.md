# LPD Climate Harvester for Vectorworks

**Instant, accurate climate data for Manual J & Manual S — directly inside Vectorworks.**

A clean, production-ready BIM workflow tool that automates climate data retrieval for residential HVAC load calculations.

---

### Who This Is For

Mid-level Vectorworks-certified architects and draftsmen who want **fast, accurate, code-compliant** climate data without leaving the BIM environment or paying for expensive third-party services.

---

### What It Does

Enter any U.S. ZIP code → instantly get:

- IECC Climate Zone + Moisture Regime
- Heating Design Temperature (99%)
- Cooling Design Temperature (1%)
- Coincident Wet Bulb
- Grains Difference (Latent Load)
- HDD / CDD (Base 65)
- Ground Temperatures (Winter / Summer)
- Recommended R-values & U-values
- Clear **Real Data** vs **Fallback** indicators

Export a clean single-row CSV that drops straight into your existing `manual_j_dataset` worksheet — no reformatting required.

---

### Key Features

- **34-column professional dataset** optimized for Vectorworks
- **Single-row export** — tiny, clean files perfect for worksheets
- **Manual J** worksheet template (ready to import)
- **Manual S** worksheet template with oversizing Pass/Fail checks
- **Sample Vectorworks file** with Space styles + building envelope plugin objects already linked
- Professional Streamlit web app (no installation needed)
- Full Python source code available on GitHub
- Transparent data sourcing (NOAA + ASHRAE + eeweather)

---

### Quick Start (Recommended)

#### Option 1: Web App (Fastest — No Installation)

1. Go to: [https://lpd-climate-harvester.streamlit.app/](https://lpd-climate-harvester.streamlit.app/)
2. Enter your project ZIP code
3. Click **Download CSV for Vectorworks**
4. In Vectorworks: **File → Import → CSV** → select the downloaded file
5. Import into your existing **`manual_j_dataset`** worksheet (overwrite or append as needed)
6. Your Manual J and Manual S will populate automatically

#### Option 2: Local Run (For Customization)

```bash
git clone https://github.com/livingpropertydesigns/manual-j-harvester.git
cd manual-j-harvester
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/main.py          # Generates full 33,782-row dataset
streamlit run app.py        # Launches local web app
```

---

### Vectorworks Workflow

1. **Import the climate data**
   - Download the single-row CSV from the web app (or run the harvester locally)
   - Import directly into your existing **`manual_j_dataset`** worksheet
   - This is the same worksheet your Manual J already references via VLOOKUP

2. **Manual J Worksheet**
   - All climate data (heating_99, cooling_1, grains_diff, iecc_zone, ground temps, HDD/CDD, etc.) pulls automatically
   - No manual data entry required

3. **Manual S Worksheet**
   - Pulls loads from Manual J
   - Calculates equipment oversizing percentages
   - Shows clear **PASS / FAIL** based on ACCA guidelines
   - Includes IECC zone, grains, and ground temperatures for documentation

4. **Sample File**
   - Includes pre-linked Space styles
   - Building envelope plugin objects (walls, roofs, floors, windows, doors) already connected
   - Ready-to-run Manual J + Manual S worksheets

---

### What's Included in the Sample Folder

```
LPD_Climate_Harvester_Sample/
├── README.md
├── Manual_J_Worksheet_Template.csv          ← Import into manual_j_dataset
├── Manual_S_Worksheet_Template.csv          ← With oversizing Pass/Fail
├── manual_j_zip_lookup.csv                  ← Full 34-column reference (optional)
├── Sample_Vectorworks_File.vwx              ← Pre-linked Space styles + envelope objects
├── docs/
│   ├── user-guide.md
│   ├── vectorworks-setup.md
│   └── troubleshooting.md
└── images/                                  ← Screenshots for documentation
```

---

### Data Sources & Transparency

- **Primary**: eeweather (lat/long → IECC zone)
- **Design Temperatures**: ASHRAE county data (via Tabula extraction)
- **Degree Days**: NOAA 1991–2020 normals
- **Fallbacks**: Clearly labeled when county-level data is incomplete

For Yavapai County, AZ we include verified local values (22°F heating / 97°F cooling).

---

### Philosophy

This tool was built to solve a real problem in our own office.  
It has been used and approved by local authorities on every residential project since late 2024.

We’re releasing it **completely free** because good tools should help more people build homes faster and with less friction.

If it saves you time, that’s the win.  
If you improve it or expand it (Manual D, Marionette, etc.), we’d love to hear from you.

---

### License

**MIT License** — Use it, modify it, share it.  
Just don’t sell it as your own.

---

### Credits

Built with care by **Living Property Designs, LLC**  
with significant assistance from Grok (xAI).

Special thanks to the Vectorworks community for the inspiration and the platform that makes tools like this possible.

---

**Let’s keep building homes and creating families.**

*Last updated: April 2026*