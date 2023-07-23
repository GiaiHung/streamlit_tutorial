import streamlit as st
import pandas as pd
import seaborn as sns

st.set_option("deprecation.showPyplotGlobalUse", False)

# TITLE
st.title("Data Analysis")
st.subheader("Data Analysis with Python and Streamlit")

# UPLOAD DATASET
upload = st.file_uploader("Upload your dataset in CSV format")
if upload is not None:
    data = pd.read_csv(upload)

# DISPLAY DATASET
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

# CHECK DATATYPE OF EACH COLUMN
if upload is not None:
    if st.checkbox("Check Datatype"):
        st.write(data.dtypes)

# DATA SHAPE
if upload is not None:
    if st.checkbox("Check Data Shape"):
        shape = data.shape
        st.write("Number of rows: ", shape[0])
        st.write("Number of columns: ", shape[1])

# FIND NULL VALUES IN DATASET
if upload is not None:
    if st.checkbox("Check Null Values in Dataset"):
        isnull = data.isnull().values.any()
        if isnull == True:
            sns.heatmap(data.isnull())
            st.pyplot()
        else:
            st.success("Congratulations! There is no null values in your dataset")

# REMOVE DUPLICATES
if upload is not None:
    if st.checkbox("Check Duplicated Values in Dataset"):
        is_duplicated = data.duplicated().any()
        if is_duplicated == True:
            st.warning("This dataset contains duplicated values!")
            duplicate = st.selectbox(
                "Do you want to remove it?", ("Select one", "Yes", "No")
            )
            if duplicate == "Yes":
                data = data.drop_duplicates()
                st.text("Duplicated values have been removed!")
            elif duplicate == "No":
                st.text("OK. No problem :)")
        else:
            st.success("Congrats! There is no duplicated values in ypur dataset")

# OVERALL STATISTICS
if upload is not None:
    if st.checkbox("Summary statistics of dataset"):
        st.write(data.describe(include="all"))

# ABOUT AND BY SECTION
st.subheader("Proudly built with Streamlit")
if st.button("Developer"):
    st.subheader("Truong Giai Hung")
