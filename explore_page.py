import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("londonciki_public_survey.csv")




# @st.cache_data(experimental_allow_widgets=True)
def show_explore_page():

    st.title("Explore Pyramid Poverty Scale ")
    st.subheader("Explore more on Poverty measurement alongside Londonciki")


    st.write(
       """
       ### poverty measurement in londonciki in the year 2023.
        """
    )

# plt.plot(,label="AUC")
# plt.title('income and population ,londonciki')
# plt.ylabel('population')
# plt.xlabel('income')
# plt.legend(loc=4)





# data = df["Population","income",].value_counts()
# data = pd.read_csv("londonciki_public_survey3.csv")
# data = np.array(data)
#
# fig1, ax1 = plt.subplots()
# ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
# ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

# st.write("""#### Number of Data from different population SampleDetermination""")
# #
# st.pyplot(fig1)
#



    st.write(
        """
            #### Mean income Based Of londonciki dwellers

        """
        )





    data = df.groupby(["income"])[("Population")].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.line_chart(data)

    st.area_chart(data)
    st.write(
         """
        #### standard deviation of income based in londonciki

        """
        )

    data = df.groupby(["income"])["Population"].std().sort_values(ascending=True)
    st.line_chart(data)

# st.write(
#     """
#     mean area chat of income based of londonciki
#     """
# )
# data = df.groupby(["income"])["Population"].mean().sort_values(ascending=True)
# st.area_chart(data)
#
# #
# data = df.groupby(["income"])["Population"].mean().sort_values(ascending=True)
# st.area_chart(data)
#
# st.pyplot(df)

    # st.scatter_chart(data)

    st.write(
        """
         Showcase of Londonciki Position Toward Poverty.
    """
    )


    st.scatter_chart(df)
    st.bar_chart(data)


    st.write("Education Status")
    st.image("./edu1.jpg")
    st.image("./edu2.jpg")


    st.write(" Access to Water ")
    st.image("./water.png")
    st.image("./water ss.png")

    st.write("Source of Power")
    st.image("./elec.png")

    st.write(" Transportation Channel")
    st.image("./road.png")
    st.image("./trans1.png")

    st.write("Drainage case")
    st.image("./drain.png")
    st.image("./float.png")









# import matplotlib.pyplot as plt
# labels = 'From','Hogs','Dogs','Logs'
# sizes = [15, 30, 45, 10]
# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels)
#
# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels, autopct='%1.1f%%')
#
#



    # st.write("Developed by MGT")
    # st.write("© University of Maiduguri,2023")
    #
    #
