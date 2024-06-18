import streamlit as st


def BMI_calculator(height,weight):
    try:
        height = float(input("請輸入身高(cm):")) / 100
        weight = float(input("請輸入體重(kg):"))
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            result = f"您好！您的BMI為{bmi:.2f}, 體重過輕")
        elif bmi < 24:
            result = f"{name}您好！您的BMI為{bmi:.2f}, 屬於正常範圍"
        elif bmi < 27:
            result = f"{name}您好！您的BMI為{bmi:.2f},體重過重 "
        elif bmi < 30:
            result = f"{name}您好！您的BMI為{bmi:.2f},屬於輕度肥胖 "
        elif bmi < 35:
            result = f"{name}您好！您的BMI為{bmi:.2f},屬於中度肥胖 "
        else:
            result = f"{name}您好！您的BMI為{bmi:.2f},屬於重度肥胖 "
        
        return result

    except:
        result =  "輸入格式錯誤"
        return result



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
weight = st.number_input("請輸入體重",step=0.5,value=50.0,max_value= 500.0,min_value=15.0)
with st.form("BMI calculator"):
    
    st.session_state['height'] = height
    st.session_state['weight'] = weight

    st.write("您的身高:",st.session_state.height,"公分")
    st.write("您的體重:",st.session_state.weight,"公斤")
            
    submitted = st.form_submit_button(label="計算", use_container_width=True)

if submitted:
    result_string = BMI_calculator(st.session_state.height,st.session_state.weight)

    result_area = st.empty()
    with result_area:
       st.write(result_string)
    

st.divider()

st.markdown('''
                 
|  | 身體質量指數(BMI)  $$(kg/m^2)$$ | 腰圍  (cm) |
| :-----| :----: | :----: |
| 體重過輕 | BMI ＜ 18.5 | - |
| 正常範圍 | 18.5≦BMI＜24 | - |
| 異常範圍 | * 過重：24≦BMI＜27  * 輕度肥胖：27≦BMI＜30  * 中度肥胖：30≦BMI＜35  * 重度肥胖：BMI≧35 | * 男性：≧90公分  * 女性：≧80公分 |      
''')

st.markdown('''
_參考來源[亞東醫院](https://depart.femh.org.tw/dietary/3OPD/BMI.htm)_
''')