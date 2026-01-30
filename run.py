from core.data import countries
from core.model import calculate_resilience
from core.shocks import apply_shock
from core.explain import explain_impact

shock_type = "health"
shock_intensity = 0.1
for country_name, metrics in countries.items():
  baseline = calculate_resilience(metrics)
  post_shock = apply_shock(baseline, shock_intensity)
  explanation = explain_impact(country-name, shock_type)
  print(f"Country: {country_name}")
  print(f"Baseline Score: {baseline}")
  print(f"Post-Shock Score: {post_shock}")
  print(f"Impact Explanation: {country_name}")
  print("_"*40)

