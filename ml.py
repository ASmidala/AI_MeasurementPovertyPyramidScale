
import streamlit as st
from measure_page import show_measure_page
from explore_page import show_explore_page
from whitepaper_p import show_whitepaper_page
from PIL import Image


image = Image.open("./visualize2.png")
st.image(image,width=180)
page = st.sidebar.selectbox("Explore,Measure,Whitepaper",("Measure", "Explore","Whitepaper"))


base="dark"
primarycolor="dark-black"
backgroundColor="black"
secondaryBackgroundColor="gray"
# textColor="black"
font="sans-serif"

if page == "Measure":
      show_measure_page()
elif page == "Explore":
      show_explore_page()
else:
      show_whitepaper_page()


st.write("Developed by MGT")
st.write("© University of Maiduguri,2023")