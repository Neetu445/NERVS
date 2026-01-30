def calculate_resilience(metrics: dict) -> float:
  """calculates average resilience score from all metrics"""
  total = 0
  for value in matrics.values():
    total += value

score = total/len(metrics)
return round(score,2)
