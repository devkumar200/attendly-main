import streamlit as st
import base64

def header_home():
    logo_path = "D:\\Attendly\\logo.png"

    with open(logo_path, "rb") as image_file:
        logo_url = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;margin-top:30px;margin-bottom:30px;">
        <img src='data:image/png;base64,{logo_url}'style='height:100px'/>
        <h1 style='text-align:center;color:#FAFAFA'>Attendly</h1>
        </div>

    """,unsafe_allow_html=True)


def header_dashboard():
    logo_path = "D:\\Attendly\\logo.png"

    with open(logo_path, "rb") as image_file:
        logo_url = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <div style="display:flex;align-items:center;justify-content:center;gap:10px;">
        <img src='data:image/png;base64,{logo_url}'style='height:85px'/>
        <h2 style='text-align:left;color:#5865F2'>Attendly</h1>
        </div>

    """,unsafe_allow_html=True)