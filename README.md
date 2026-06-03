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
5. Import into your existing **manual_j_dataset** worksheet (overwrite or append as needed)
6. Your Manual J and Manual S will populate automatically

#### Option 2: Local Run (For Customization)

```bash
git clone https://github.com/livingpropertydesigns/lpd-climate-harvester.git
cd lpd-climate-harvester
python3 -m venv venv
source venv/bin/activate          # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py