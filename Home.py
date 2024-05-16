import streamlit as st
import cv2
import numpy as np
from st_config import set_cfg
import time
from streamlit_card import card

st.set_page_config(page_title='AI Analytics', page_icon="👥", layout="wide", initial_sidebar_state="auto", menu_items=None)
st.markdown(set_cfg.ahana_logo, unsafe_allow_html=True) 
st.markdown(set_cfg.hide_bar, unsafe_allow_html=True) 
st.markdown(set_cfg.show_bar, unsafe_allow_html=True) 
st.markdown(set_cfg.ahana_logo, unsafe_allow_html=True) 
st.markdown(set_cfg.hide_streamlit_style, unsafe_allow_html=True) 
st.markdown(set_cfg.hide_deploy_btn,unsafe_allow_html=True)
st.markdown(set_cfg.st_tabs,unsafe_allow_html=True)
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.markdown(set_cfg.hide_img_fs, unsafe_allow_html=True)


st.header('Alerts')
st.divider()

col1,col2,col3,col4,col5,col6=st.columns(6)



with col1:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='1',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})
with col2:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='2',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})
with col3:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='3',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})
with col4:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='4',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})
with col5:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='5',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})
with col6:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='6',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})




with col1:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='7',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})
with col2:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='8',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})
with col3:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='9',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})
with col4:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='10',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})
with col5:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='11',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})
with col6:
    card1=card(title="Perimeter Breach!",text="Some description",image="https://t3.ftcdn.net/jpg/03/62/97/08/360_F_362970887_phPgPN3vHxpi8v3eGt1yoXyneIYlz2Fe.jpg",key='12',styles={"card": {"width": "220px","height": "220px","border-radius": "40px"}})


st.divider()