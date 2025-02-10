import streamlit as st
from streamlit_extras.stylable_container import stylable_container

st.image("https://gifdb.com/images/high/cute-love-bear-roses-ou7zho5oosxnpo6k.gif", width = 1000)
st.write("## Hola Boo, will you be my Valentines?")
col1_, col2_, col3_ = st.columns([1,1,8])
with col1_:
    button_yes = st.button("Yes", type = "primary")
with col2_:
    with stylable_container(
    "red",
    css_styles="""
    button {
        background-color: #FF0000;
        color: white;

    }""",
    ):
        button_no = st.button("No", disabled = True)

    
with col3_:
    pass

if button_yes:
    st.write("##### Wuuuuuuuuuuuuuuuu")
    st.image("https://i.gifer.com/2rDV.gif", width = 1000)
    st.write("##### Te quiero muchisimo booo :heart:")
    st.write("#### Muakyy")
    st.image("https://media1.tenor.com/m/lwowvCpVB1cAAAAd/kiss-otter.gif", width = 1000)