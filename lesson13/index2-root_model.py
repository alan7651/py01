import streamlit as st
import source
from source import Root

data_str = source.download_youbike()
root = Root.model_validate_json(data_str)
data = root.model_dump()

print(data)
def ijk(value):
    return value['行政區']

areas:list[str] = list(set(map(ijk,data)))

option = st.selectbox("請選擇行政區",areas)
st.write("您選擇:", option)