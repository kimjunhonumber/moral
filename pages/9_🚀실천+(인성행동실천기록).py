import streamlit as st
from streamlit_gsheets impoort GSheetsConnection
import pandas as pd
import matplotlib.pyplot as plt


url ="https://docs.google.com/spreadsheets/d/1KksuDA2ZjkkNanlZXlw_t7iE7okYnI_UMxJZz8Lzl60/edit?gid=0#gid=0("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, uescols=list(range(2)), worksheet="0#gid=0")
st.dataframe(data)
