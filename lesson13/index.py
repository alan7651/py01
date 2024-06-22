import streamlit as st

def BMI_calculator(height,weight):
    try:
        height = float(height) / 100 #身高cm轉公尺
        weight = float(weight)
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
        
        print(result)
        return result

    except:
        result =  "輸入格式錯誤"
        return result

st.subheader("🐷BMI值計算")
st.divider()
st.latex('''
         BMI值計算公式:BMI = 體重(公斤) / 身高^2(公尺^2)
         ''')
st.latex("例如：一個52公斤的人，身高是155公分，則BMI為:")
st.markdown('''
<h6 style="color:blue;text-align:center">52(公斤) / 1.552 ( 公尺<sup>2</sup> ) = 21.6</h6>
<h6 style="color:orange;text-align:center">體重正常範圍為 BMI = 18.5～24</h6>
<hr style="border:0;margin:0 auto;width:80%;border-top:2px dotted blue">
<h6 style="color:purple;text-align:center;margin-top:18px">快看看自己的BMI是否在理想範圍吧!</h6>
''',unsafe_allow_html=True)

height = st.slider(":blue[請選/擇身高]",min_value = 120, max_value=230,value =155)  
weight = st.number_input(":blue[請輸入體重]",step=0.5,value=50.0,max_value= 500.0,min_value=15.0)

with st.form("BMI_Calculator",clear_on_submit=True):

    st.session_state['height'] = height
    st.session_state['weight'] = weight

    st.write("您的身高:",height,"公分")
    st.write("您的體重:",weight,"公斤")

    if st.form_submit_button(label="確認並計算", use_container_width=True):
        result_string = BMI_calculator(height=st.session_state.height,weight=st.session_state.weight)

        with st.container(border=True):
            st.subheader(result_string)   
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

