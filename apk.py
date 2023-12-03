import streamlit as st
import pickle
import numpy as np
import pandas
import matplotlib
import pandas

# from pickle import dump
# from pickle import load

#
# #
# # model=pickle.load(open('model.pkl','rb'))
# # def predict_poverty(Passiveincome_education_healthcare_MPi):
# #     input=np.array([[Passiveincome_education_healthcare_MPi]]).astype(np.float64)
# #     measurement=model.predict_status(input)
# #     measure='{0:.{1}f}'.format(measurement[0][0], 2)
# #     print(type(measure))
# #     return float(measure)
# #
# # def main(Passiveincome_education_healthcare_MPi):
# #     st.title("Pyramid Poverty Scale")
# #     html_temp = """
# #     <div style="background-color:#025246 ;padding: 10px">
# #     <h2 style="color:white;text-align:center;">Poverty Measurement ML App(Nigeria in respect of London Ciki)</h2>
# #     </div>
# #     """
# #
# #     st.markdown(html_temp, unsafe_allow_html=True)
# #
# #     income = st.text_input("Income", "Type here")
# #     education = st.text_input("Education", "Type here")
# #     healthcare = st.text_input("Healthcare", "Type here")
# #     MP = st.text_input("Multidimensional Poverty", "Type Here")
# #     safe_html="""
# #        <div style=background-color:#f4003F;padding:10px >
# #        <h2 style="color:white;text-align:center;"> Status above the poverty line , safe line </h2>
# #        </div>
# #     """
# #
# #     danger_html="""
# #        <div style=background-color:#000000;padding:10px >
# #        <h2 style="color:black;text-align:center;"> Status below the Poverty line , Danger alert </h2>
# #        </div>
# #     """
# #
# #     if st.button("Measure/Scale"):
# #         output=predict_poverty(Passiveincome_education_healthcare_MPi)
# #         st.success('the Status of Poverty is {}'.format(output))
# #
# #     if output >= 60000:
# #             st.markdown(danger_html,unsafe_allow_html=True)
# #     else:
# #             st.markdown(safe_html,unsafe_allow_html=True)
# #
# # if __name__== '___main___':
# #     main()
#
#
# import streamlit as st
# import pickle
# import numpy as np
# model=pickle.load(open('model.pkl','rb'))
#
#
# # def show_measure_page():
# def predict_poverty(income_mpi_education_healthcare):
#     input=np.array([[income_mpi_education_healthcare]]).astype(np.float64)
#     prediction=model.predict_proba(input)
#     pred='{0:.{1}f}'.format(prediction[0][0], 2)
#     print(type(pred))
#     return float(pred)
#
#
# def main():
#
#        st.title("Pyramid Poverty Scale")
#        html_temp = """
#           <div style="background-image:url("visualize.png");size=cover ">
#           <div style="background-color:#025246 ;padding: 10px">
#            <h2 style="color:white;text-align:center;">Poverty Measurement AI/ML App(Nigeria in Boundry of London Ciki)</h2>
#            </div>
#          """
#        st.markdown(html_temp,unsafe_allow_html=True)
#
#
# income = st.text_input('IncomePerMonth','Type Here')
# mpi = st.text_input('Multidimensional poverty index','Type Here')
# education = st.text_input('Education Status or Level','Type Here')
# healthcare = st.text_input('Healthcare Standard','Type Here')
# safe_html = """
#            <div style=background-color:green;padding:10px >
#             <h2 style="color:white;text-align:center;"> Status above the poverty line , safe line . source according to official poverty measurement(OPM)
#             and UN standard Poverty Per Person(PPP) range.</h2>
#             </div>
#         """
# danger_html = """
#             <div style=background-color:red;padding:10px >
#             <h2 style="color:black;text-align:center;"> Status below the Poverty line , Danger alert . source according to official poverty  measurement(OPM)
#             and UN Poverty Per Person(PPP) range. </h2>
#             </div>
#         """
# if st.button('Measure/Scale'):
#     output=predict_poverty(income,mpi,education,healthcare)
#     st.success("the poverty status level is {}".format(output))
#
#     if output >  60100:
#             st.markdown(danger_html,unsafe_allow_html=True)
#     else:
#         st.markdown(safe_html,unsafe_allow_html=True)
#
#
# footer1_html = """
#              <div style=font-size:italic;padding:10px>
#              <h2 style=color:"black;text-align:center;">Developed by MGT<h2>
#              <div>
# """
# st.markdown(footer1_html,unsafe_allow_html=True)
# footer2_html = """
#           <div style=font-size:italic;padding:10px>
#              <h2 style=color:"black;text-align:center;">© University of Maiduguri, 2023<h2>
#              <div>
# """
# st.markdown(footer2_html,unsafe_allow_html=True)
#
# if __name__=='__main__':
#      main()


import matplotlib.pyplot as plt

labels = 'From','Hogs','Dogs','Logs'
sizes = [15, 30, 45, 10]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels, autopct='%1.1f%%')
#

