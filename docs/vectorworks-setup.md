# Vectorworks Setup Guide

## Step-by-Step Workflow

### 1. Prepare Your Vectorworks File
- Your file must follow standard Vectorworks organization:
  - Consistent **Design Layers**
  - Proper **Plugin Styles** for Spaces, Walls, Slabs, Ceilings, Roofs, Doors, Windows, etc.
- Adjust the **database header search criteria** in the Manual J worksheet to match your file (sample criteria included in the template).

### 2. Import Climate Data
1. Run the LPD Climate Harvester (web or local)
2. Export the CSV
3. In Vectorworks: **File > Import > CSV**
4. Import as a worksheet named **ZIP_Lookup**

### 3. Link the Worksheets
The Manual J worksheet uses `VLOOKUP` formulas to pull climate data from the **ZIP_Lookup** worksheet.

### 4. Use the Manual S Worksheet
Import `Manual_S_Worksheet_Template.csv` as a new worksheet named **Manual_S**. It will automatically pull heating and cooling loads from your Manual J worksheet.