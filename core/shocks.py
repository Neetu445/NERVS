def apply_shock(baseline_score: float, shock_intensity:float) -> float:"""Applies a shock to a country's baseline resilience score
shock_intensity:value between 0 and 1"""
  reduced_score = baseline_score*(1-shock_intensity)

return round(max(reduced_score, 0), 2)
