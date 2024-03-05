import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
from babel.numbers import format_currency
sns.set(style='dark')

seasonal_df = pd.read_csv("seasonal.csv")
conditions_df = pd.read_csv("weathers.csv")

st.header('Bike Sharing Dashboard')

st.subheader('Banyaknya Pengguna Rental Sepanjang Musim')
 
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(seasonal_df['season'], seasonal_df['casual'], marker='o', linewidth=2, color="#ffd678",label="Casual")
ax.plot(seasonal_df['season'], seasonal_df['registered'], marker='o', linewidth=2, color="#59B4C3",label="Registered")
ax.plot(seasonal_df['season'], seasonal_df['cnt'], marker='o', linewidth=2, color="#332c92",label="Total")
ax.grid()
ax.legend()

st.pyplot(fig)

st.subheader('Banyaknya pengguna rental terhadap kondisi cuaca yang berbeda')

x = np.arange(len(conditions_df['total_group']))
width = 0.25

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, conditions_df['Clear'], width, label='Clear',color="#332c92")
rects2 = ax.bar(x, conditions_df['Misty'], width, label='Misty', color= "#59B4C3")
rects3 = ax.bar(x + width, conditions_df['Light Weather'], width, label='Light Weather',color="#ffd678")

ax.set_xticks(x)
plt.xlabel("Dalam satuan perorangan",fontsize=8)
ax.set_xticklabels(conditions_df['total_group'])
ax.legend()

fig.tight_layout()

st.pyplot(fig)
 
st.caption('Copyright (c) Muhammad Ilyasa Rafi Azhar 2024')