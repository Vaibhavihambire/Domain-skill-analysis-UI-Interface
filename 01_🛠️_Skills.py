import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from modules.formater import Title
from modules.importer import DataImport
import ast

# Title page and footer
title = "🛠️ Skills"
t = Title().page_config(title)
# Import data
jobs_all = DataImport().fetch_and_clean_data()
st.markdown("## 🛠️ Domain Skills Analysis")
# Job Title dropdown
job_title = st.selectbox('Select Job Title', jobs_all['Job_Title'].unique())

# Filter data based on selected job title
filtered_data = jobs_all[jobs_all['Job_Title'] == job_title]




# Extract and count skills
skills_count = {}
total_jobs = len(filtered_data)
for skills_list in filtered_data['Job_Skills']:
    skills_list = ast.literal_eval(skills_list)  # Convert string representation to list
    for skill in skills_list:
        skills_count[skill] = skills_count.get(skill, 0) + 1

# Calculate percentages and define color ranges
max_percentage = max(skills_count.values()) / total_jobs * 100
color_scale = alt.Scale(
    domain=[0, max_percentage * 0.25, max_percentage * 0.5, max_percentage],
    range=['lightblue', 'skyblue', 'deepskyblue', 'dodgerblue']
)

# Create DataFrame for skills
skills_df = pd.DataFrame({'Skill': list(skills_count.keys()), 'Count': list(skills_count.values())})
skills_df['Percentage'] = skills_df['Count'] / total_jobs * 100

# Create a bar chart
bar_chart = alt.Chart(skills_df).mark_bar().encode(
    x=alt.X('Percentage:Q', axis=alt.Axis(format='%'), title='Percentage of Jobs'),
    y=alt.Y('Skill:N', axis=alt.Axis(title='Skills'), sort='-x'),
    color=alt.Color('Percentage:Q', scale=color_scale, legend=None)
)

# Add percentage labels
text = bar_chart.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text=alt.Text('Percentage:Q', format='.1f')  # Format percentage to one decimal place
)

# Display the chart
st.altair_chart((bar_chart + text), use_container_width=True)
