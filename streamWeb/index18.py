import streamlit as st


def BMI_calculator():
     try:
         height = float(st.session_state.height) / 100 #身高cm轉公尺
         weight = float(st.session_state.weight)
         bmi = weight / (height ** 2)
 
         if bmi < 18.5:
             result = f"您好！您的BMI為【{bmi:.2f}】, 體重過輕"
         elif bmi < 24:
             result = f"您好！您的BMI為【{bmi:.2f}】, 屬於正常範圍"
         elif bmi < 27:
             result = f"您好！您的BMI為【{bmi:.2f}】, 體重過重 "
         elif bmi < 30:
             result = f"您好！您的BMI為【{bmi:.2f}】, 屬於輕度肥胖 "
         elif bmi < 35:
             result = f"您好！您的BMI為【{bmi:.2f}】, 屬於中度肥胖 "
         else:
             result = f"您好！您的BMI為【{bmi:.2f}】,屬於重度肥胖 "
 
     except:
         result =  "輸入格式錯誤"
 
     st.session_state['BMI_result'] = result

st.header("🐷 BMI值計算")
st.divider()
 
with st.expander(":blue-background[查看解釋]", expanded=True):
      st.markdown('''
 ### BMI值計算公式:    
 ##### $$ BMI = 體重(公斤) / 身高^2 (公尺^2)$$
 - _例如：一個52公斤的人，身高是155公分，則BMI為 :_
 >  $$52(公斤)/1.552 ( 公尺^2 )= 21.6$$  
 > _體重正常範圍為  BMI=18.5～24_
 
 ''')
      st.markdown('''
     _參考來源[亞東醫院](https://depart.femh.org.tw/dietary/3OPD/BMI.htm)_
     ''')
 
st.subheader("快看看自己的BMI是否在理想範圍吧!")
height = st.slider("請選擇身高",min_value = 120, max_value=230,value =155)  
weight = st.number_input("請輸入體重",step=0.5,value=50.0,max_value= 500.0,min_value=15.0)
with st.form("BMI calculator"):
     
     st.session_state['height'] = height
     st.session_state['weight'] = weight
 
     st.write("您的身高:",st.session_state.height,"公分")
     st.write("您的體重:",st.session_state.weight,"公斤")
             
     submitted = st.form_submit_button(label="確認並計算", use_container_width=True,on_click=BMI_calculator )

if submitted:
    with st.container(border=True):
        st.subheader(st.session_state.BMI_result)   
        st.markdown('''
    <style>
    .alignment{
    text-align:left;       
    }
  
    </style>

     |  | 身體質量指數(BMI)  $$(kg/m^2)$$ | 腰圍  (cm) |
     | :-----| :----: | :----: |
     | 體重過輕 | BMI ＜ 18.5 | - |
     | 正常範圍 | 18.5≦BMI＜24 | - |
     | 異常範圍 | <ul class="alignment"> <li>過重：24≦BMI＜27</li><li>輕度肥胖：27≦BMI＜30</li><li>中度肥胖：30≦BMI＜35</li><li>重度肥胖：BMI≧35</li></ul> | <ul class=alignment><li>男性：≧90公分</li><li>女性：≧80公分</li></ul> |      
   
    ''',unsafe_allow_html=True)
     
     
        st.markdown('''
     _參考來源[亞東醫院](https://depart.femh.org.tw/dietary/3OPD/BMI.htm)_
     ''')