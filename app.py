#----Creating a Website----

import streamlit as st


#create the name in the tab menu
st.set_page_config(page_title="Contact Us", page_icon=":Happy:", layout="wide")



#-------Header Section-------

st.subheader("Hi, My name is Karim Mohamed ")
st.title("Karim")
st.write("Shebin Elkom Elmonofeya")




#----What i do Section---- 


with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i Do in my life")
        st.write("##")
        st.write("Hello")
        st.write("[instagram account >](https://www.instagram.com/karimmohamed04/)")
