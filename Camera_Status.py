import streamlit as st
import cv2
import numpy as np
from st_config import set_cfg
import time
import cv2



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


st.sidebar.header('Filter Options')

@st.experimental_dialog("Update Incident",width="large")
def vote(id):
    c1,c2,c3=st.columns([1,10,1])
    stop_btn=c2.button('Stop Streaming',use_container_width=True,type='primary')

    c2=c2.empty()
    cap = cv2.VideoCapture('samples/sample.mp4')
    if not cap.isOpened():
        print("Error: Unable to open video file.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        c2.image(frame)
        if stop_btn:
           cap.release()


@st.experimental_dialog("Captured Image",width="large")
def view_img(id):
    st.image('1.png')
    if st.button('Close Image',use_container_width=True):
        st.rerun()

cam_status_sel=st.sidebar.multiselect("**:black[Filter By Camera Status]**",("Active", "Inactive"),label_visibility='visible')
area_sel=st.sidebar.multiselect("**:black[Filter By Area ]**",("Area1", "Area2"),label_visibility='visible')
pgn=st.sidebar.radio('**:black[Number Of Records To Display]**',[10,20,30],horizontal=True,index=0)
filter_btn=st.sidebar.button('Apply Filters',use_container_width=True,type='primary')
st.sidebar.divider()

sc1,sc2,sc3=st.sidebar.columns([2,2,2])
sc1.metric("**:green[Total Cameras ]**","100")
sc2.metric("**:green[🟢 Active ]**","80")
sc3.metric("**:red[🔴 Inactive ]**","20")
st.sidebar.divider()


st.subheader('Camera Status 📄')

cc1,cc2,cc3=st.columns([0.1,10,0.1])
cc2.divider()
c1,c2,c3=st.columns([0.1,10,0.1])
colms = c2.columns((2, 2, 2, 2, 1, 1, 1, 2,1))
fields = ["Cam ID",'Cam Name','Cam Type','Cam IP','Cam Port','Cam Location','Status','View Details','Test']
cam_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]


c2.divider()
for col, field_name in zip(colms, fields):
    col.markdown(f'**{field_name}**')


for x in range(0,len(cam_ids),1):
    col1, col2, col3, col4, col5,col6,col7,col8,col9 = c2.columns((2, 2, 2, 2, 1, 1, 1, 2,1))
    col1.markdown(f'**:black[{cam_ids[x]}]**')  
    col2.markdown('Camera 1')
    col3.markdown('Bullet IR')
    col4.markdown('192.168.120.20')
    col5.markdown('5543')
    col6.markdown('Admin Office')
    col7.markdown(':green[Active 🟢]')

    with col8.popover("View",use_container_width=True):
        st.markdown('Camera IP : ')
        st.markdown('Camera Port : ')
        st.markdown('Camera Type : ')
        st.markdown('Camera Provider : ')
        st.markdown('Installed Location : ')
        st.markdown('Camera Status : ')
        st.markdown('Active Since : ')
        st.markdown('')

    disable_status = 'active'
    button_type = "Unblock" if disable_status else "Block"
    button_phold = col9.empty()
    update_button = button_phold.button('Test', key=str(x),use_container_width=True,type="primary")
    if update_button:
         pass
         vote(x)
 
c2.divider()









