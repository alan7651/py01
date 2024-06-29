import streamlit as st
import source
from source import Root

try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e,icon="💔")
else:
    root = Root.model_validate_json(data_str)
    data = root.model_dump()
    
    print(data)
    def ijk(value):
        return value['行政區']
    
    areas:list[str] = list(set(map(ijk,data)))

    def change_area():
        st.write(st.session_state)
    
    if 'area' not in st.session_state:
        st.session_state['area'] = "八里區"
    
    with st.sidebar:
        option = st.selectbox(":orange[行政區：]",options = areas,index=None,placeholder="請選擇行政區",on_change=change_area,key="area")
        if option != None:
            st.write("目前選擇:", option)