import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.style_base_layout import style_base_layout,style_background_home

def home_screen():
    # st.header("Home screen",text_alignment='center')

    header_home()

    style_background_home()
    style_base_layout()

    col_1,col_2 = st.columns(2,gap="large")

    with col_1:
        st.header("I'm Student")
        st.image("student.png",width=120)
        if st.button('Student Portal',type="primary",icon=':material/arrow_outward:',icon_position="right"):
            st.session_state['login_type'] = 'student'
            st.rerun()         

    with col_2:
        st.header("I'm Teacher")
        st.image("teacher.png",width=120)
        if st.button('Teacher Portal',type="primary",icon=':material/arrow_outward:',icon_position="right"):         
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()
       