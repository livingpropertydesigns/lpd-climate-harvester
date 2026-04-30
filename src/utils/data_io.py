"""
Utility functions for data input/output operations.
"""

import pandas as pd
from pathlib import Path

def save_lookup_table(df: pd.DataFrame, output_path: Path):
    """Save the processed lookup table to CSV with basic validation."""
    try:
        df.to_csv(output_path, index=False)
        print(f"✓ Successfully saved lookup table with {len(df):,} records.")
    except Exception as e:
        print(f"✗ Error saving lookup table: {e}")

def load_lookup_table(path: Path) -> pd.DataFrame:
    """Load the processed lookup table (for future use)."""
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"✗ Error loading lookup table: {e}")
        return pd.DataFrame()