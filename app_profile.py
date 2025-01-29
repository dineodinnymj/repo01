#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:04:46 2025

@author: maboreraseala
"""

import streamlit as st
import panda as pd

#Title of the app 
st.title("Researcher Profile Page")

#Collect basic information
name = "Mabore Jerida Raseala"
field = "Chemistry"
institution = "University of South Africa"
institute = "Institute for Nanotechnology and Water Sustainabilty"

#Dispaly basic profile information
st.header("Research Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of research:** {field}")
st.write(f"**Institution:** {institution}")
st.write(f"**Institute:** {institute}")

#Add a section for publications 
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publication", type = "csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)
    
    #Add filtering for years or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications [publications.apply(lambda row: keyword.lower().values, axis = 1)]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else: 
        st.write(f"Showind all publications")
        
#Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns : 
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize treands.")
        
#Add a contact section
st.header("Contact Information")
email = "dineodinnymj@gmail.com"
st.write(f"You can reach {name} at {email}")
        
