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

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.sidebar.header('Filter Options')

@st.experimental_dialog("Update Incident",width="large")
def vote(id):
 
    remarks=st.text_area('Remarks ')
    if st.button("Submit"):
        st.success('done')
        time.sleep(1)
        st.rerun()

@st.experimental_dialog("Captured Image",width="large")
def view_img(id):
    st.image('1.png')
    if st.button('Close Image',use_container_width=True):
        st.rerun()

st.subheader('Manage Incidents 📄')

inc_type=st.sidebar.multiselect("**:black[Select Incident Type]**",("Active", "Closed"),label_visibility='visible')
inc_zone_sel=st.sidebar.multiselect("**:black[Select Area]**",("Thermal Plant", "Admin Office", "Electric Stations","Other Areas"),label_visibility='visible')
pgn=st.sidebar.radio('**:black[Number Of Records To Display]**',[10,20,30],horizontal=True,index=0)
filter_btn=st.sidebar.button('Apply Filters',use_container_width=True,type='primary')
st.sidebar.divider()

sc1,sc2,sc3=st.sidebar.columns([2,2,2])
sc1.metric("**:green[Total Incidents ]**","100")
sc2.metric("**:green[🟢 Active ]**","80")
sc3.metric("**:red[🔴 Inactive ]**","20")
st.sidebar.divider()

    
cc1,cc2,cc3=st.columns([0.1,10,0.1])
cc2.divider()
c1,c2,c3=st.columns([0.1,10,0.1])
colms = c2.columns((2, 2, 2, 2, 1, 1, 1, 2,1))
fields = ["Alert ID",'Alert Name','Date & Time','Location','Status','Time Elapased','View Image','Select Option','Action']
ticket_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]


c2.divider()
for col, field_name in zip(colms, fields):
    col.markdown(f'**{field_name}**')


for x in range(0,len(ticket_ids),1):
    col1, col2, col3, col4, col5,col6,col7,col8,col9 = c2.columns((2, 2, 2, 2, 1, 1, 1, 2,1))
    col1.markdown(f'**:black[{ticket_ids[x]}]**')  
    col2.markdown('Perimeter breach')
    col3.markdown('2022-20-21 23:22')
    col4.markdown('Thermal plant')
    col5.markdown(':green[Active 🟢]')
    col6.markdown('3 Hr')
    with col7.popover("View",use_container_width=True):
        st.image('1.png')
    option = col8.selectbox("",("Close", "Re-assign", "Mark as Fasle"),key=str(x)+'k',label_visibility='collapsed')
    

    #c2.divider()
    disable_status = 'active'
    button_type = "Unblock" if disable_status else "Block"
    button_phold = col9.empty()
    update_button = button_phold.button('Update', key=str(x),use_container_width=True,type="primary")
    if update_button:
         pass
         vote(x)
 
c2.divider()