# Changelog

All notable changes to the Manual J Climate Harvester will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
- Switched from Tabula-extracted county data to improved processing
- Removed all temporary debug code and manual overrides
- Finalized production-ready codebase

### Notes
- First stable release
- Optimized for Arizona work with national coverage
- Some counties (e.g., Yavapai) currently use safe fallback values due to source data limitations

---

## [0.9.0] - 2026-04-20

### Added
- Initial working harvester with ZIP, FIPS, IECC, and ASHRAE integration
- Streamlit prototype UI
- Basic psychrometric grains calculation

### Changed
- Major refactoring of data pipeline
- Improved error handling and fallback logic

---

*This project is under active development. Future versions will include Vectorworks integration, expanded shading calculations, and multi-state data improvements.*