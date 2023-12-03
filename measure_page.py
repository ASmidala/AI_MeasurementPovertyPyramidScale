# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('londonciki_public_survey.csv')
#
# def show_measure_page():
#     st.title("Pyramid Poverty Scale")
#     st.write("""### We need some information to Measure Poverty status """)
#     st.title(""" Pyramid Poverty Scale """)
#
# st.write("""### We need some information to Measure Poverty status """)
#
#
# education = (
#              40,
#              70,
#               90,
#              )
#
# HealthcareStatus = (
#     60,
#     80,
#     100,
# )
#
# Location = st.selectbox("Location:",("Location",'London-Ciki'))
#
# Mpi = st.slider("Multidimensional poverty index", 0.1,0.6,1.0)
#
# Education  = st.selectbox("Education",('40%','70%', '90%'))
# Healthcare  = st.selectbox("Healthcare",('60%', '80%', '100%'))
# income = st.text_input("Income", "")
#
# html_background = """
#  <style>
#  body{
#
#  background-image: url("visualize.png");
#  background-repeat: no-repeat;
#  background-attachment: fixed;
#  background-size: 100 100%;
#  </style>
# """
#
#
# html_temp = """
#       <div style="background-image:url("visualize.png"); size: cove">
#       <div style="background-color:#025246 ;padding: 10px">
#        <h2 style="color:white;text-align:center;">Poverty Measurement ML App(Nigeria in respect of London Ciki)</h2>
#        </div>
#      """
#
#
#
#
# safe_html="""
#        <div style=background-color:green;padding:10px >
#         <h2 style="color:white;text-align:center;"> Status above the poverty line , safe line </h2>
#         </div>
#     """
#
#
# danger_html="""
#         <div style=background-color:red;padding:10px >
#         <h2 style="color:black;text-align:center;"> Status below the Poverty line , Danger alert </h2>
#         </div>
#      """
#
#
# if st.button("Measure/Scale"):
#     output=income("income","education","healthcare","MPi")
#     st.success('the Status of Poverty is {}'.format(output))
#
#
# if income ==60000:
#          st.markdown(danger_html,unsafe_allow_html=True)
# else:
#      st.markdown(safe_html,unsafe_allow_html=True)


# ml.py(testing the  model)
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle



warnings.filterwarnings("ignore")


data = pd.read_csv("londonciki_public_survey3.csv")
data = np.array(data)



X = data[1:, 1:-1]
y = data[1:, -1]
y = y.astype('int')
X = X.astype('int')
#print(X,y)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=0)
log_reg = LogisticRegression()


log_reg.fit(X_train, y_train)

pickle.dump(log_reg,open('model.pkl','wb'))

inputt=[int(x) for x in "45 32 60".split(' ')]
final=[np.array(inputt)]


#  app.py to  train  the model

import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))




def predict_poverty(income,mpi,healthcare):
    inputt=np.array([[income,mpi,healthcare]]).astype(np.float64)
    prediction=model.predict_proba(inputt)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    print(type(pred))
    return float(pred)


# def main():
def show_measure_page():
    st.title("Pyramid Poverty Scale")
    html_temp = """
           <div style="background-image:url("visualize.png");size=cover ">
          <div style="background-color:#025246 ;padding: 10px">
           <h2 style="color:white;text-align:center;">Poverty Measurement AI/ML App(Nigeria in Boundry of London Ciki)</h2>
           </div>
         """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write("Fill the Require Space")
    income = st.text_input('IncomePerMonth','Type Here')
    mpi = st.text_input('Multidimensional poverty index','Type Here')
    healthcare = st.text_input('Healthcare Standard','Type Here')


    safe_html = """
           <div style=background-color:green;padding:10px >
            <h2 style="color:white;text-align:center;"> Status above the poverty line , safe line . thus: official poverty measurement(OPM)
            and see also: UN standard  Per Person Income(PPI) range.</h2>
            </div>
        """
    danger_html = """
            <div style=background-color:red;padding:10px >
            <h2 style="color:black;text-align:center;"> Status below the Poverty line , Danger alert .thus: official poverty  measurement(OPM)
            and see also: UN  Per Person Income(PPI) range. </h2>
            </div>
        """
    if st.button('Measure/Scale'):
        output=predict_poverty(income,mpi,healthcare)
        st.success("the probability poverty status level is {}".format(output))
        if output > 0.5:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)


       # footer1_html = """
       #       <div style=font-size:italic;padding:10px>
       #       <h2 style=color:"black;text-align:center;">Developed by MGT<h2>
       #       <div>
       # """
       # st.markdown(footer1_html,unsafe_allow_html=True)
       # footer2_html = """
       #    <div style=font-size:italic;padding:10px>
       #       <h2 style=color:"black;text-align:center;">© University of Maiduguri, 2023<h2>
       #       <div>
       # """
       # st.markdown(footer2_html,unsafe_allow_html=True)

    # st.write("Developed by MGT")
    # st.write("© University of Maiduguri,2023")

if __name__=='__show_measure_page__':
     show_measure_page()