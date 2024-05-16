import streamlit as st
import cv2
import numpy as np
from st_config import set_cfg
import time



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


st.header('Page coming soon!')
st.balloons()

