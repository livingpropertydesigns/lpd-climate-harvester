# Changelog

All notable changes to the Manual J Climate Harvester will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-04-29

### Added
- **eeweather** integration as primary climate zone source (accurate IECC + moisture regime from lat/long)
- Improved county name matching for ASHRAE data
- Transparent `data_source` column (`Real`, `Real (verified)`, `Fallback (known good)`)
- Final production testing success for Yavapai County (ZIP 86303 → 4B / 22.0°F / 97.0°F)
- Clean, sustainable fallback system for counties with incomplete source data

### Changed
- Removed all temporary debug code and hard-coded overrides
- Switched from Gist-based IECC to eeweather for accuracy and reliability
- Finalized output structure matching original `climate_data.csv` format

### Notes
- This is the first fully stable, production-ready release
- Optimized for real-world BIM workflows (especially Arizona)
- Some counties still use verified fallback values due to source data limitations — clearly labeled in output

---

## [1.0.0] - 2026-04-28

### Added
- Complete ZIP-to-climate data pipeline (33,782 records)
- IECC Climate Zone lookup with FIPS mapping
- ASHRAE design temperatures (Heating 99%, Cooling 1%, Coincident WB)
- Safe fallback system for counties with incomplete source data
- Streamlit UI with real-time lookup
- Clear **Real Data** vs **Fallback** indicators
- Basic shading / solar gain reference calculator
- CSV export formatted for Vectorworks worksheet import
- Clean, modular Python architecture
- Professional documentation (README, CONTRIBUTING, LICENSE, CHANGELOG)

### Changed
- Major refactoring of data pipeline
- Improved error handling and fallback logic

---

*This project is under active development. Future versions will include full Manual S template, Vectorworks integration, and NOAA 1991–2020 normals support.*