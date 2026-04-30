# LPD Climate Harvester

**Accurate Climate Data for Vectorworks Manual J + Manual S**

A professional BIM workflow tool that automates climate data retrieval for **Manual J** residential load calculations directly inside Vectorworks.

---

### What It Does

- Takes a ZIP code and returns accurate IECC climate zone + ASHRAE design temperatures
- Uses **eeweather** for precise climate zones
- Exports clean CSV data ready for Vectorworks worksheets
- Includes a complete **Manual S** worksheet template with automatic load linking

---

### Quick Start

**Option 1: Web App (Recommended)**  
Visit: [https://lpd-climate-harvester.streamlit.app](https://lpd-climate-harvester.streamlit.app)

**Option 2: Run Locally**

```bash
git clone https://github.com/yourusername/lpd-climate-harvester.git
cd lpd-climate-harvester

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python src/main.py          # Generate climate data
streamlit run app.py        # Launch the UI