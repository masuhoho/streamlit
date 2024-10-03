import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("Bike Sharing Dataset")

st.subheader("Pengelompokkan Jumlah Penyewaan Sepeda Berdasarkan Musim")

day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
day_df['season'] = day_df['season'].map(season_mapping)

grouped_data = day_df.groupby('season')['cnt'].sum()

colors = ['red' if val == grouped_data.max() else 'lightgray' for val in grouped_data]

fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(grouped_data.index, grouped_data.values, color=colors)

ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Musim")

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 20, 
            int(bar.get_height()), ha='center', va='bottom')

st.pyplot(fig)

st.subheader("Pengelompokkan Jumlah Penyewaan Sepeda Berdasarkan Jam")

grouped_data = hour_df.groupby('hr')['cnt'].sum()

colors = ['red' if val == grouped_data.max() else 
          'blue' if val == grouped_data.min() else 
          'lightgray' for val in grouped_data]

fig, ax = plt.subplots(figsize=(15, 8))
bars = ax.bar(grouped_data.index, grouped_data.values, color=colors)

ax.set_xticks(range(0, 24, 1))  
ax.set_xticklabels(range(0, 24, 1))
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Jam")

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 20, 
            int(bar.get_height()), ha='center', va='bottom')

st.pyplot(fig)

