import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar as navbar
import os
from PIL import Image
import pandas as pd
import numpy as np

image = Image.open('img/logo.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

logo_path = os.path.join(os.path.dirname(__file__), "img", "bear.svg")
pages = [" ",'Home','Project1', 'Project2', 'Project3']

styles = {
    "nav": {
        "background-color": "rgba(154, 154, 254)",
        "display": "flex",
        "justify-content": "center"
    },
    "img": {
        "position": "absolute",
        "left": "-12px",
        "font-size": "16px",
        "top": "4px",
        "width": "111px",
        "height": "55px",
    },
    "div":{
        "max-width":"32rem",
    },
    "span":{
        "border-radius":"0.5rem",
        "color":"rgba(50,60,60)",
        "margin":"0 0.125rem",
        "padding":"0.4375rem 0.625rem",
    },
    "active":{
        "background-color":"rgba(154,154,255,0.25)",
        "color": "black",
        "font-weight": "normal",
        "padding": "14px",
    },
    "hover":{
        "background-color":"rgba(255,255,255,0.35)",
    },
}
options = {
    "show_menu": False,
    "show_sidebar": True,
}


page = navbar(pages, styles=styles, logo_path=logo_path, options=options)

if page == 'Home':
    Home.Home().app()
elif page == 'Project1':
    Project1.Project1().app()
elif page == 'Project2':
    Project2.Project2().app()
elif page == 'Project3':
    Project3.Project3().app()
else:
    Home.Home().app()