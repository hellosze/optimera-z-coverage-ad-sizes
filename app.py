import streamlit as st
import file_utils

z_impressions_file = st.file_uploader('Upload Z Impressions.csv')  
ron_impressions_file = st.file_uploader('Upload RON Impressions.csv')  

if z_impressions_file is not None:  
  z_impressions_df = pd.read_csv(z_impressions_file)  
else:  
  st.stop() 

ron_impressions_file = st.file_uploader('Upload RON Impressions.csv')  
if ron_impressions_file is not None:  
  ron_impressions_df = pd.read_csv(ron_impressions_file)  
else:  
  st.stop() 
