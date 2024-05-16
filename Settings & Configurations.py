import streamlit as st
import cv2
import numpy as np
from st_config import set_cfg
import time
import extra_streamlit_components as stx

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




chosen_id = stx.tab_bar(data=[
    stx.TabBarItemData(id=1, title="Camera Settings", description=""),
    stx.TabBarItemData(id=2, title="Alerts Configurations", description=""),
    stx.TabBarItemData(id=3, title="Video Analytics Settings", description=""),
    stx.TabBarItemData(id=4, title="Misc Settings", description=""),
], default=1)

c1,c2,c3,c4=st.columns([2,0.5,4,8])

def camera_settings():
    c3.text('')
    c3.text('')
    c1.subheader('camera settings')
    add_cam_btn=c1.button('Add Camera',use_container_width=True)
    view_cam_btn=c1.button('View Cameras',use_container_width=True)
    modi_cam_btn=c1.button('Modify Camera',use_container_width=True)
    rm_cam_btn=c1.button('Remove Camera',use_container_width=True)
    test_cam_btn=c1.button('Test Camera',use_container_width=True)

    if add_cam_btn:
        with c3.expander('Add new camera',expanded=True):
            cam_id=st.text_input('Enter Camera ID')
            cam_name=st.text_input('Enter Camera Name')
            cam_type=st.text_input('Enter Camera Type')
            cam_loc=st.text_input('Enter Camera Location')
            cam_ip=st.text_input('Enter Camera IP')
            cam_port=st.text_input('Enter Camera Port')
            cam_url=st.text_input('Enter Camera RTSP URL')
            save_cam_btn=st.button('Save Camera',use_container_width=True,type='primary')


        








if chosen_id == '1':
    camera_settings()




#val = stx.stepper_bar(steps=["Ready", "Get Set", "Go","Ready", "Get Set", "Go"])
#st.info(f"Phase #{val}")