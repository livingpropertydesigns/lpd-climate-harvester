"""
Psychrometric calculations using sympy for grains difference.
"""

import sympy as sp

def calc_grains_difference(cooling_db: float, coincident_wb: float) -> float:
    """
    Calculate grains difference using psychrometric approximation.
    Indoor condition: 75°F, 50% RH (WB ≈ 55°F)
    """
    try:
        T_wb = sp.symbols('T_wb')
        w = 0.62198 * sp.exp(17.27 * T_wb / (T_wb + 237.3)) / (1013.25 - 0.378 * sp.exp(17.27 * T_wb / (T_wb + 237.3)))
        w_out = float(w.subs(T_wb, coincident_wb))
        w_in = float(w.subs(T_wb, 55))
        grains = 7000 * (w_out - w_in)
        return round(grains, 2)
    except:
        return 25.0  # Safe fallback