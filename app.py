import streamlit as st
st.title(':red[Innomatics] Data App :sunglasses:')
st.header('Data Scinece Internship')
st.subheader("Feb 2023")
#Code= '''print('hello world')'''
#st.code(Code, language='python')
btn_click = st.button("About me")
if btn_click== True:
    st.write('''My name is Vikas Pandey. I an aspiring Data Analyst with a B.Tech degree and proven problemsolving skills. Seeking an entrylevel Data Analysis aor data Science job to continue
expanding my knowledge.''')
    st.balloons()