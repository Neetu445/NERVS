def explain-impact(country: str, shock_type: str) -> str:
""" Generates a human-readable explanation for why a country's resilience changed."""

reasons = {
  "health": "Healthcare systems were overwhelmed, reducing response capacity.", 
  "economic": "Economic instability weakened recovery mechanism.",
  "cyber":"Cyber Infrastructure faced sustained digital attacks.",
  "energy":"Energy supply distruptions affected national stability.",
  "conflict":"Geopolitical tensions strained defense and resources."}

reason = reasons.get(shock-type, "Multiple interconnected systemic stresses affected resilience.")
return f"{country} experienced a decline in resilience because{reason}"
  
                    
