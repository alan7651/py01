import streamlit as st
import source
from source import Root
import pandas as pd

try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e,icon="💔")
else:
    root = Root.model_validate_json(data_str)
    data = root.model_dump()
    #print(data)

    def ijk(value):
        return value['行政區']
    
    areas:list[str] = list(set(map(ijk,data)))

    st.title("新北市Youbike 站點資料")
    result_container = st.container()
    table_container = st.container(height=700,border=False)

    def change_area():
        area = st.session_state.area
        display_data = [item for item in data if item['行政區'] == area ]
        
        with table_container:
            st.subheader(f"{area} 共有{len(display_data)}筆資料：")
            result_pd = pd.DataFrame(data=display_data,
                                    columns=["站點名稱","日期時間","地址","總數","可借","可還",'經度','緯度'])
            
            option_pd = st.selectbox(options=result_pd)
            st.dataframe(data=option_pd)

            st.map(result_pd,
                latitude='緯度',
                longitude='經度',
                size='總數')
            
    
    with st.sidebar:
        option = st.selectbox(":orange[行政區：]",options = areas,index=None,placeholder="請選擇行政區",on_change=change_area,key="area")
        if option != None:
            st.write("目前選擇:", option)

