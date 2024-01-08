import streamlit as st 
import pandas as pd
import altair as alt
import seaborn as sns

st.title("Palmer's Penguins")

# Read in data and display first 5 rows
penguins_df = pd.read_csv("penguins_app\penguins.csv")
st.write(penguins_df.head())

# Create dropdowns for the inputs to the interactive visualization
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

penguin_file = st.file_uploader('Select your local Penguins CSV - default is None')

if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    #st.stop()
    penguins_df = pd.read_csv("penguins_app\penguins.csv")

selected_x_var = st.selectbox('What do you want the x variable to be?', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
                                                                         'body_mas_g'])
selected_y_var = st.selectbox('What about your y variable?', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm',
                                                                         'body_mas_g'])
selected_gender = st.selectbox('What gender do you want to filter for?', ['All', 'Male', 'Female'])

sns.set_style('darkgrid')
markers = {'Adelie': 'X', 'Gentoo':'s', 'Chinstrap':'0'}

# Filter the dataframe based on the given variables
if selected_gender == 'Male':
    penguins_df = penguins_df[penguins_df['sex']=='male']
elif selected_gender == 'Female':
    penguins_df = penguins_df[penguins_df['sex']=='female']
else:
    pass

alt_chart = (alt.Chart(penguins_df, title=f"Scatterplot of {selected_gender} Penguins").mark_circle().encode(x=selected_x_var, 
                                                                                        y=selected_y_var, color='species')).interactive()
st.altair_chart(alt_chart, use_container_width=True)