# src/stdash/app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title("CNN JOB MON")

def load_data():
    url = "http://43.202.66.118:8077/all"
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)
df['request_time'] = pd.to_datetime(df['request_time'])

df.index = df['request_time']
grouped = df.groupby(pd.Grouper(freq='H')).size()
grouped = grouped.reset_index()
grouped.columns = ['request_time', 'count']

grouped

plt.bar(grouped['request_time'].astype(str), grouped['count'], alpha=0.6)
plt.plot(grouped['request_time'].astype(str), grouped['count'], color='red')

plt.xlabel('Request Time')
plt.ylabel('Count')
plt.title('Requests per Hourly Interval')
plt.xticks(rotation=45)
plt.legend()
st.pyplot(plt)
