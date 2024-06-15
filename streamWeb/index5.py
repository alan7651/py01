import streamlit as st

st.bar_chart({"data": [1, 2, 3, 2, 2, 4]})

with st.expander(":blue-background[查看解釋]", expanded=True):
    st.markdown('''
## The chart above shows some numbers I picked for you.
- I rolled actual dice for these
- so they're *guaranteed* to
> be random.

''')
