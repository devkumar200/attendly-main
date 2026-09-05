import streamlit as st
import base64

def footer_home():
    logo_path = "Devas_logo.png"

    with open(logo_path, "rb") as image_file:
        logo_url = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <div style="margin-top:2rem;display:flex;gap:6px; justify-content:center;align-items:center">
        <p style="font-weight:bold;color:white;">Created by Devashish Prajapati</p>
        <img src='data:image/png;base64,{logo_url}'style='max-height:40px'/>
        </div>

    """,unsafe_allow_html=True)



def footer_dashboard():
    logo_path = "Devas_logo.png"

    with open(logo_path, "rb") as image_file:
        logo_url = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <div style="margin-top:2rem;display:flex;gap:6px; justify-content:center;align-items:center">
        <p style="font-weight:bold;color:black;">Created by Devashish Prajapati</p>
        <img src='data:image/png;base64,{logo_url}'style='max-height:40px'/>
        </div>

    """,unsafe_allow_html=True)