import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
# Title of the Streamlit app
st.title('Excel Data Visualization')
 
# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])
 
# Function to read Excel file and plot graph
def plot_graph(data):
    # Read Excel file into a DataFrame
    df = pd.read_excel(data)
   
    # Display the DataFrame
    st.write("Data from Excel file:")
    st.write(df)
   
    # Get column names
    column_names = list(df.columns)
   
    # Select the first two columns for plotting
    x_axis = "Project Name"
    y_axis = st.selectbox("Select Y-axis", column_names[1:])
   
    # Plot the graph using seaborn
    st.write("Graph:")
    sns.set_style("whitegrid")
    sns.barplot(x=x_axis, y=y_axis, data=df)
    plt.xticks(rotation=90)
    st.pyplot()
    showPyplotGlobalUse = "false"
 
# Check if file is uploaded
if uploaded_file is not None:
    plot_graph(uploaded_file)
