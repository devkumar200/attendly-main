import streamlit as st
from src.database.db import delete_subject
from src.database.config import supabase


@st.dialog("Remove Subject")
def remove_subject_dialog(subject_id,teacher_id,subject_name):

    st.write(f"Are you sure you want to remove **{subject_name}**?")

    col1,col2 = st.columns(2)

    with col1:
        if st.button("Cancel",width="stretch"):
            st.rerun()

    with col2:
        if st.button(
            "Remove",
            type="primary",
            icon=":material/delete:",
            width="stretch"
        ):
            delete_subject(subject_id,teacher_id)
            st.toast(f"{subject_name} removed successfully!")
            st.rerun()