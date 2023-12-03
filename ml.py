# import numpy as np
# import pandas as pd
# # from sklearn.linear_model import LogisticRegression
# # from sklearn.model_selection import train_test_split
# # import warnings
# # import pickle
# # warnings.filterwarnings("Ignore")
# import matplotlib
# import warnings
# import pickle
# warnings.filterwarnings("ignore")
#
# data = pd.read_csv("LondonCiki_Survey2.csv")
# data = np.array(data)
#
# X = data[1:, 1:-1]
# y = data[1:, -1]
# y = y.astype('int')
# X = X.astype('int')
# #print(X,y)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# log_reg = LogisticRegression()
#
# log_reg.fit(X_train, y_train)
#
# pickle.dump(log_reg_open('model.pkl','wb'))
#
# inputt=[int(x) for x in "60000 700000 1000 000".split(' ')]
# final=[np.array(inputt)]



import streamlit as st
from measure_page import show_measure_page
from explore_page import show_explore_page
from PIL import Image



image = Image.open("./visualize2.png")
st.image(image,width=180)
page = st.sidebar.selectbox("Explore Or Measure", ("Measure", "Explore"))



base="dark"
primarycolor="dark-black"
backgroundColor="black"
secondaryBackgroundColor="black"
# textColor="black"
font="sans-serif"

if page == "Measure":
      show_measure_page()
else:
      show_explore_page()

st.write("Developed by MGT")
st.write("© University of Maiduguri,2023")