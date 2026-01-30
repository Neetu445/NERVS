import streamlit as st
st.set_page_config(page_title="NERVS", layout="wide")

st.title("NERVS")
st.subheader("National Elastic Resilience & Vulnerability System")

st.write("""NERVS is an AI-driven stress-test engine that models how contries absorb,
amplify, and recover from global shocks.""")

st.header("Input Country Stress Indicators")

countries=["India", "China","USA", "Japan", "Russia"]

indicators = ["Economic Stability,
              "Defence & Security", "Healthcare Readiness", "Cyber Infrastructure", "Energy Security"]
data ={}

for country in countries:
  st.subheader(country)
  data[country] = {}
  for indicator in indicators:
    value = st.slider(f"{indicator} ({country})",
                      min-value=1,
                      max_value=10,
                      value= 5,
                      key=f"{country}_{indicator}")
    data[country][indicator] = value
import pandas as pd

#AI scoring logic
weights={ "Economic Stability": 0.2, "Defence & security":0.2, "Healthcar Readiness":0.2, "Cyber Infrastructure":0.2, "Energy Security":0.2}

score{}
explanation ={}
# calculate score for each country
for country, value in data.items():
  score = sum(value[ind]* weights[ind] for indin weights)
  scores[country = round(score,2)
  strongest = max(values, key=value.get)
  weakest = min(values, key=value.get)
  explanations[country] = f"Strongest:{strongest}, Weakest:{weakest}"

#display result
st.header("Resilience Scores")

df = pd.DataFrame({"Country": score.keys(),
                   "Resilience Score": scores.values()})
st.dataframe(df)


import matplotlib.pyplot as plt
st.header("Resilience Comparison")

fig, ax = plt.subplots()
ax.bar(scores.key(), scores.values(), color="skyblue") 
ax.set_ylabel("Resilience Score")
ax.set_yli(0,10)

st.pyplot(fig)

st.header("Stress Scenerio Siulation")

scenerio = st.selectbox("select a Global Stress Scenerio",["None", "Economic Crisis", "Cyber Attack", "Pandemic", "Energy Shock"])

scenerio_impact = {"Economic Crisis": {"Economic Stability": -2}, "Cyber Attack":{Cyber Infrastructure": -3}, 
                   "Pandemic":{Healthcare Readiness": -3}, "Energy Shock": {"Energy Security": -3}, "None":{}
} 
    adjusted_scores = {}        
    impact_explanation ={}
for country, values in data.items():
                      adjusted_values =values.copy()
for ind, impact in scenerio_impact[scenerio].items():
  adjusted_values[ind] = max(1,adjusted_values[ind]+ impact)

  new_score = sum(adjusted_values[ind]* weights[ind] for ind in weights)
  adjusted_scores[country] = round(new_score,2)

  impact_explanations[country] = (f"scenerio'{scenerio}' reduced {list(scenerio_impact[scenerio].key())}"
                                  if scenerio !="None"
                                  else"No external stress applied")

# impacted result
st.header("Post-Shock Resilience Scores")

impact_df = pd.DataFrame({"Country": adjusted_scores.key(), "Post-Shock Score": adjusted_scores.values(), "Impact Explanation": impact_explanations.values()})

st.DataFrame(impact_df)

st.header("Pre-Shock vs Post-shock Comparison")

comparison_df = pd.DataFrame({"Country": baseline_scores.keys(), "Base-line Score": baseline_scores.values(), "Post-Shock": adjusted_scores.values()})

st.dataframe(comparison_df)

#bar chart
st.subheader("Resilience Change Visualization")

st.bar_chart(comparison_df.set_index("Country"))

st.header("Key Insights")

for country, explanation in impact_explanations.items():
  st.markdown(f"**{country}**-> {explanation}")
  st.markdown("_ _ _")
  st.markdown("**NERVS - Nationsl Evaluation & Resilience Vector System**")
  st.caption("AI-Driven Dynamic Stress-Testing Engine")  
            
                                     
