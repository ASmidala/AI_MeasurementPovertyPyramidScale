# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





# df = pd.read_csv("LondonCiki_Survey2.csv")
# st.slider("Uber Pickup in NYC")
# st.subheader('Number of pickups by hour')
#
# # hist_values = np.histogram(
# #        data[DATA_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#
# # st.bar_chart(hist_values)
#
# st.subheader('Map of all pickups')
#
# # st.map(data)
# st.title('Poverty pyramid scale1.0')
# st.header('Prediction of Poverty in londonciki using AI')
# st.subheader('Measurement/ Scale London-Ciki')
# st.text('AI PROJECT')
# st.markdown('here is with sample determination of 60 people')
# st.latex(r''' e{i\pi} + 1 = 0''')
# st.write('most object')
# st.write(['st', 'is <', 3])
# st.code('for i in range(59): foo()')
#
# # st.df("LondonCiki_Survey2.CSV")
# st.table(df.iloc[0:10])
# st.json({'foo':'bar','fu':'ba'})
# st.metric('the metric', 42, 2)
# element = st.dataframe(df)
# element .add_rows(df)
# element = st.line_chart(df)
# element = st.bar_chart(df)
# # element = st.graphviz_chart(df)
# element.add_rows(df)
#
# st.image('./visualize.png')
# st.audio('./audio.mp3')
# st.video('video.mp4')
#
# # element = st.empty()
# # element.line_chart()
# # element.text_input()
#
# st.area_chart(df)
# st.bar_chart(df)
# st.line_chart(df)
# # st.map(df)
# st.scatter_chart(df)
#
# # st.altair_chart(df)
# # st.bokeh_chart(df)
# # st.graphviz_chart(df)
# # st.plotly_chart(df)
# # st.pydeck_chart(df)
# # st.pyplot(df)
# # # st.vega_lite_chart(df)
# #
# # elements = st.container()
# # elements.line_chart(...)
# # st.write("Hello")
#
# # st.help(pandas,DataFrame)
# # st.get_option(key)
# # st.set_page(key, value)
# # st.set_page_config(layout='wide')
# # st.experimental_get_query_params()
# # st.experimental_set_query_params(**params)
# #
# # st.experimental_connection('pets. db', type='sql')
# # conn = st.experimental_connection('sql')
# # conn = st.experimantal_connection('snowpark')
#
# # class Myconnection(ExperimantalBaseConnection[myconn
# #     def _connect(self, **kwargs) -> Myconnection:
# #          return myconn.connect(**self._secrets, **kwar
# #     def query(self, query):
# #         return self._instance.query(query)
# #
# #         )])
# #
# #         @st.cache_data
# #         def foo(bar):
#
# # d2 = foo(f2)
# # d3 = foo(ref2)
# #
# # foo.clear()
# # st.cache_data.clear()
# #
# # @st.cache_resource
# # def  foo(bar):
# #     rerun  = session
# #
# # s1 = foo(ref1)
# # s2 = foo(ref1)
#
#
#
# a = st.sidebar.radio('select one:', [1, 2])
# st.sidebar.selectbox("Measure Poverty or  Explore more:",('Measure/Scale ','Explore more'))
#
# with st.sidebar:
#     st.multiselect("M OR E:", ('P ', 'E'))
#
#
# col1, col2, col3 = st.columns(3)
# col2.write("Location")
# col2.write('income')
# col3.write('mpi')
#
# col1, col2, col3 = st.columns([3, 1, 1])
# col1.write("Location")
# col2.write('mpi')
# col3.write('income')
#
# tab1, tab2 = st.tabs(["Tab 1","Tab 2"])
# tab1.write("poverty status")
# tab2.write("scale of poverty")
#
# # st.button('explore')
# # st.toggle("poverty scale ")
# # st.radio("measurement of poverty",("income", "mpi"))
# # st.selectbox("pps","education","healthcare")
# # st.multiselect("mpps", ("mpi","income"))
# # st.slider("size",["I",'MPI','EDU','healthcare'])
# # st.text_area("Fiest name")
# # st.date_input("p a number", 0,10)
# # st.text_area("translate")
# # st.date_input('your birthday')
# # st.time_input('meeting time')
# # st.file_uploader('upload a csv')
# # st.camera_input("Take a picture")
# # st.color_picker("pick a color")
#
# # for i in range(int(st.number_input('Num:'))):
# #     foo()
# # if st.slider.selectbox('I:',['F'] == 'f'
# #   b()
# # my_slider_val = st.slider('Quin Mallormy', 1, 88)
# #   st.write(slider_v)
#
# #time.sleep(3)
# st.success('Done!')
#
#
# # st.balloons()
# st.snow()
# st.toast('Warming up...')
# st.error('there is error')
# st.warning('warning message')
# st.info('info we are good')
# st.success("succesfully in")
#
# # if st.user.email == 'unimaid@gmail.com':
# #     display_unimaid_content()
# # elif st.user.email == 'mgt@gmail.com':
# #     display_mgt_content()
# # else:
# #      st.write("Please contact5 us to get access!")
# # #     # st.exception(e)
#
# # bar = st.progress(50)
# # bar.progres(100)
#
# # st.download_button("Download:translate file", df)
# # st.link_button("Go to gallery", url)
# # st.data_editor("Edit data", df)
# # st.checkbox("I agree")
#
# with st.form(key='my_form'):
#
#  username = st.text_input('username')
#  password = st.text_input('Password')
#  st.form_submit_button('Login')
#
#
# with tab1:
#     st.radio('PS OR SS:', ('PS','SS'))
#
# st.stop()
#
# st.rerun()
#
#
#
#
# with col1:
#     st.selectbox('select:','location')
#
# with st.echo():
#     st.write('poverty measured successfully!')
# st.subheader("pyramid poverty scale")
# st.write("Poverty")
# st.selectbox("Location:",("London-Ciki"))
# st.slider("education")
# st.slider("healthcare")
# st.slider("multidimensional poverty index")
#
#
#
# # DATE_Column = 'date/time'
# # DATA_URL = ('https://s3-us-west-2.amazon.com/'
# #             'streamlit-demo-data/uber-raw-sep14.csv.gz ')
# #
# #
# # @st.cache_data
# # def load_data(nrows):
# #     data = pd.read_csv("DATA_URL, nrows=nrows")
# #     lowercase = lambda x: str(x).lower()
# #     data.rename(lowercase, axis='column', inplace=True)
# #     data[DATE_Column] - pd.to_datetime(data[DATE_Column])
# #     return data
# #
# # data_load_state = st.text('Loading data...')
# # data = load_data(10000)
# # data_load_state.text("Done! (using st.cache data)")
# #
# #
# # if st.checkbox('Show raw data'):
# #     st.subheader('Raw data')
# #     st.write(data)
# #
# # st.subheaader('Number of pickups by  hour')
# # hist_values = np.histogram(data[DATE_Column].dt.hour, bins=24, range=(0,24))[0]
# # st.bar_chart(hist_values)
# #
# #
# # hour_to_filter = st.slider('hour', 0,23,17)
# # filtered_data = data[data[DATE_Column].dt.hour == hour_to_filter]
# #
# #
