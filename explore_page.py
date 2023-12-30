import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("londonciki_public_survey.csv")




# @st.cache_data
def show_explore_page():

    st.title("Explore Pyramid Poverty Scale ")
    st.subheader("Explore more on Poverty measurement alongside Londonciki")


    st.write(
       """
       ### poverty measurement in londonciki in the year 2023.
        """
    )




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











