import streamlit as st


st.header("⛄️BMI值計算")
st.divider()

with st.expander(":blue-background[查看解釋]", expanded=True):
    st.markdown('''
### BMI值計算公式:    
##### $$ BMI = 體重(公斤) / 身高^2 (公尺^2)$$
- 例如：一個52公斤的人，身高是155公分，則BMI為 :  
>  $$52(公斤)/1.552 ( 公尺^2 )= 21.6$$  
> _體重正常範圍為  BMI=18.5～24_

''')

st.subheader("快看看自己的BMI是否在理想範圍吧!")
height = st.slider("請選擇身高",min_value = 120, max_value=230,value =155)  
weight = st.number_input("請輸入體重",step=0.5,value=50.0)
with st.form("BMI calculator"):
    
    st.write("您的身高:",height,"公分")
    st.write("您的體重:",weight,"公斤")
            
    st.form_submit_button(label="計算", use_container_width=True)


result_area = st.empty()
with result_area:
    BMI = ""
    st.write(BMI)


st.divider()

st.markdown('''          
| 左对齐 | 右对齐 | 居中对齐 |
| :-----| ----: | :----: |
| 单元格 | 单元格 | 单元格 |
| 单元格 | 单元格 | 单元格 |
| 单元格 | 单元格 | 单元格 |
                
''')


    

    


st.markdown('''
_參考來源[亞東醫院](https://depart.femh.org.tw/dietary/3OPD/BMI.htm)_
''')