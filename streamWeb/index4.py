import streamlit as st
import time

with st.empty():
    for each_second in range(60):
        st.write(f"{each_second} seconds have passed")
        time.sleep(1)

    st.write("🥳 1 minute over!")
